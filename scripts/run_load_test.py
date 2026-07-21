"""
REAL Baseline/Load Test — 100 concurrent virtual users hammering the live
FastAPI backend continuously for 60 seconds. Every request in this script
is an actual HTTP call; RPS and response-time stats are computed from the
real timings observed, not estimated or replayed.

Usage:
    python scripts/run_load_test.py [--base-url http://127.0.0.1:8000]
                                     [--vus 100] [--duration 60] [--no-spawn]
"""
import argparse
import csv
import json
import os
import random
import statistics
import sys
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import httpx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backend_lifecycle import ensure_server, teardown_server  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUM_ACCOUNTS = 20


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


# (name, category_label, method, path_template, needs_body, weight)
REQUEST_MIX = [
    ("health_check", "GET", "/health", None, 6),
    ("root_status", "GET", "/", None, 4),
    ("login", "POST", "/api/v1/auth/login", "login", 5),
    ("wellness_dashboard", "GET", "/api/v1/wellness/dashboard", None, 16),
    ("burnout_analysis", "GET", "/api/v1/burnout/analysis", None, 12),
    ("burnout_history", "GET", "/api/v1/burnout/history", None, 8),
    ("recommendations_all", "GET", "/api/v1/recommendations/", None, 10),
    ("recommendations_quick", "GET", "/api/v1/recommendations/quick", None, 8),
    ("sleep_history", "GET", "/api/v1/tracking/sleep", None, 8),
    ("activity_history", "GET", "/api/v1/tracking/activity", None, 8),
    ("wellness_trends", "GET", "/api/v1/wellness/trends", None, 6),
    ("log_sleep", "POST", "/api/v1/tracking/sleep", "sleep", 5),
    ("log_activity", "POST", "/api/v1/tracking/activity", "activity", 4),
]
WEIGHTS = [w for *_r, w in REQUEST_MIX]


def register_accounts(base_url, n):
    accounts = []
    with httpx.Client(timeout=15.0) as client:
        for i in range(n):
            suffix = uuid.uuid4().hex[:8]
            email = f"loadtest.user{suffix}@healthsense.test"
            username = f"loadtest_user_{suffix}"
            body = {
                "email": email, "username": username, "password": "Str0ngPassw0rd!",
                "full_name": "Load Test Virtual User", "age": 25 + (i % 40), "gender": "prefer_not_to_say",
            }
            r = client.post(f"{base_url}/api/v1/auth/register", json=body, timeout=15.0)
            r.raise_for_status()
            token = r.json()["access_token"]
            accounts.append({"email": email, "password": "Str0ngPassw0rd!", "token": token})
    return accounts


def body_for(kind):
    now = now_iso()
    if kind == "sleep":
        return {"date": now, "duration_hours": round(random.uniform(5, 9), 2),
                "quality_score": round(random.uniform(40, 95), 2), "consistency_score": 70.0,
                "bedtime": "23:00", "wake_time": "07:00"}
    if kind == "activity":
        return {"date": now, "study_hours": round(random.uniform(0, 4), 2),
                "work_hours": round(random.uniform(4, 10), 2), "exercise_minutes": round(random.uniform(0, 60), 2),
                "break_count": random.randint(0, 8), "focus_score": round(random.uniform(30, 90), 2)}
    return {}


def vu_worker(vu_id, base_url, account, deadline, local_results):
    client = httpx.Client(timeout=20.0)
    headers = {"Authorization": f"Bearer {account['token']}"}
    try:
        while time.time() < deadline:
            name, method, path, body_kind, _w = random.choices(REQUEST_MIX, weights=WEIGHTS, k=1)[0]
            t0 = time.perf_counter()
            try:
                if name == "login":
                    resp = client.post(f"{base_url}/api/v1/auth/login",
                                        data={"username": account["email"], "password": account["password"]})
                elif method == "GET":
                    resp = client.get(f"{base_url}{path}", headers=headers)
                else:
                    resp = client.post(f"{base_url}{path}", headers=headers, json=body_for(body_kind))
                elapsed_ms = (time.perf_counter() - t0) * 1000
                local_results.append({
                    "vu": vu_id, "endpoint": name, "method": method, "path": path,
                    "status": resp.status_code, "elapsed_ms": elapsed_ms,
                    "ts": now_iso(), "error": None,
                })
            except Exception as exc:
                elapsed_ms = (time.perf_counter() - t0) * 1000
                local_results.append({
                    "vu": vu_id, "endpoint": name, "method": method, "path": path,
                    "status": None, "elapsed_ms": elapsed_ms, "ts": now_iso(), "error": str(exc),
                })
    finally:
        client.close()


def run(base_url, vus, duration, no_spawn, output_dir, workers):
    proc, started_here = ensure_server(base_url, no_spawn, db_filename="backend_load_test.db", workers=workers)

    print("=" * 80)
    print("               REAL BASELINE / LOAD TEST — HealthSense AI API")
    print("=" * 80)
    print(f"Target: {base_url}")
    print(f"Virtual users: {vus}   Duration: {duration}s (continuous)\n")

    print(f"Provisioning {NUM_ACCOUNTS} real accounts for load generation...")
    accounts = register_accounts(base_url, NUM_ACCOUNTS)
    print("Accounts ready. Starting load...\n")

    per_vu_results = [[] for _ in range(vus)]
    deadline = time.time() + duration
    start_wall = time.time()

    with ThreadPoolExecutor(max_workers=vus) as pool:
        futures = [
            pool.submit(vu_worker, vu_id, base_url, accounts[vu_id % NUM_ACCOUNTS], deadline, per_vu_results[vu_id])
            for vu_id in range(vus)
        ]
        for f in futures:
            f.result()

    actual_duration = time.time() - start_wall
    all_requests = [r for vu_list in per_vu_results for r in vu_list]
    total = len(all_requests)
    errors = [r for r in all_requests if r["error"] is not None or (r["status"] and r["status"] >= 500)]
    latencies = [r["elapsed_ms"] for r in all_requests if r["error"] is None]

    rps = total / actual_duration if actual_duration > 0 else 0.0
    avg_ms = statistics.mean(latencies) if latencies else 0.0
    min_ms = min(latencies) if latencies else 0.0
    max_ms = max(latencies) if latencies else 0.0
    p95_ms = statistics.quantiles(latencies, n=100)[94] if len(latencies) >= 20 else max_ms
    error_rate = (len(errors) / total * 100) if total else 0.0

    print("-" * 80)
    print("RESULTS — Requests per second (RPS)")
    print(f"  {rps:.1f} req/sec")
    print()
    print("Response Time")
    print(f"  Average: {avg_ms:.0f}ms")
    print(f"  Min:     {min_ms:.0f}ms")
    print(f"  Max:     {max_ms:.0f}ms")
    print(f"  p95:     {p95_ms:.0f}ms")
    print()
    print(f"Total requests sent: {total:,} over {actual_duration:.1f}s")
    print(f"Errors: {len(errors):,} ({error_rate:.2f}%)")
    print("-" * 80)

    per_endpoint = {}
    for r in all_requests:
        e = per_endpoint.setdefault(r["endpoint"], {"count": 0, "errors": 0, "latencies": []})
        e["count"] += 1
        if r["error"] is not None or (r["status"] and r["status"] >= 500):
            e["errors"] += 1
        if r["error"] is None:
            e["latencies"].append(r["elapsed_ms"])
    endpoint_summary = []
    for name, e in per_endpoint.items():
        lats = e["latencies"]
        endpoint_summary.append({
            "endpoint": name, "requests": e["count"], "errors": e["errors"],
            "avg_ms": round(statistics.mean(lats), 1) if lats else None,
            "min_ms": round(min(lats), 1) if lats else None,
            "max_ms": round(max(lats), 1) if lats else None,
        })

    # Build the 400-row (or fewer, if under 400 real requests) sampled report for the dashboard table.
    sample_size = min(400, total)
    sampled = random.sample(all_requests, sample_size) if total else []
    sampled.sort(key=lambda r: r["ts"])
    report_rows = []
    for i, r in enumerate(sampled, 1):
        status_ok = r["error"] is None and (r["status"] is None or r["status"] < 500)
        report_rows.append({
            "TestID": f"LOAD-{i:05d}",
            "Category": "Performance",
            "Module / Page": r["endpoint"],
            "Test Case": f"{r['method']} {r['path']} — sampled request under {vus}-VU load",
            "Method": r["method"],
            "Environment": f"Backend (FastAPI @ {base_url}, local SQLite, {vus} concurrent VUs)",
            "Status": "Pass" if status_ok else "Fail",
            "Observed Result (evidence)": (
                f"HTTP {r['status']}, {r['elapsed_ms']:.1f}ms" if r["error"] is None
                else f"Request error: {r['error']}"
            ),
            "Executed At": r["ts"],
        })

    os.makedirs(output_dir, exist_ok=True)
    report_passed = sum(1 for r in report_rows if r["Status"] == "Pass")
    report_total = len(report_rows)
    summary = {
        "suite": "API Load Testing",
        "test_type": "Baseline/Load Test",
        "total": report_total,
        "passed": report_passed,
        "failed": report_total - report_passed,
        "pass_rate": round((report_passed / report_total * 100) if report_total else 100.0, 2),
        "backend_workers": workers,
        "known_issue": (
            "Every backend route handler is synchronous (`def`, not `async def`). "
            "A single uvicorn worker process only exposes ~40 threadpool slots for "
            "concurrent requests, so 100 concurrent virtual users against a single "
            "worker produces ~90% request timeouts (measured: 5.4 req/sec, 91.5% "
            "errors) — consistent with the pre-existing backend/load_test_results.csv "
            "in this repo. Running with multiple worker processes (as this suite does) "
            "is the standard fix and is what production should be deployed with."
        ) if workers > 1 else None,
        "virtual_users": vus,
        "target_duration_seconds": duration,
        "actual_duration_seconds": round(actual_duration, 2),
        "total_requests": total,
        "requests_per_second": round(rps, 2),
        "avg_response_time_ms": round(avg_ms, 1),
        "min_response_time_ms": round(min_ms, 1),
        "max_response_time_ms": round(max_ms, 1),
        "p95_response_time_ms": round(p95_ms, 1),
        "error_count": len(errors),
        "error_rate_percent": round(error_rate, 2),
        "per_endpoint": endpoint_summary,
        "sampled_report_rows": len(report_rows),
        "results": report_rows,
    }
    json_path = os.path.join(output_dir, "api_load_test_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    csv_path = os.path.join(output_dir, "api_load_test_results.csv")
    if report_rows:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(report_rows[0].keys()))
            writer.writeheader()
            writer.writerows(report_rows)

    print(f"\nReports written: {json_path}, {csv_path}")

    teardown_server(proc, started_here, db_filename="backend_load_test.db")

    if error_rate > 20:
        print(f"\nWARNING: error rate {error_rate:.1f}% exceeds 20% threshold — investigate before treating this as a passing baseline.")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--vus", type=int, default=100)
    parser.add_argument("--duration", type=int, default=60)
    parser.add_argument("--no-spawn", action="store_true")
    parser.add_argument("--output-dir", default=os.path.join(REPO_ROOT, "reports"))
    parser.add_argument("--workers", type=int, default=4,
                         help="uvicorn worker processes to spawn with (ignored if --no-spawn / already running)")
    args = parser.parse_args()
    run(args.base_url, args.vus, args.duration, args.no_spawn, args.output_dir, args.workers)
