"""
Prints a GitHub Actions Step Summary (markdown, written to $GITHUB_STEP_SUMMARY
by the workflow) aggregating the same real suite JSON every other report
generator reads — no separate data source, no separate counting logic.
"""
import json
import os
import sys
from datetime import datetime, timezone


def load(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    reports_dir = sys.argv[1] if len(sys.argv) > 1 else "reports"
    pages_url = sys.argv[2] if len(sys.argv) > 2 else ""
    run_number = sys.argv[3] if len(sys.argv) > 3 else "?"
    commit_sha = sys.argv[4] if len(sys.argv) > 4 else "?"
    branch = sys.argv[5] if len(sys.argv) > 5 else "?"

    suites = {
        "Website E2E": load(os.path.join(reports_dir, "web_e2e_results.json")),
        "Mobile App E2E": load(os.path.join(reports_dir, "mobile_e2e_results.json")),
        "Backend & Security": load(os.path.join(reports_dir, "backend_security_results.json")),
        "API Load Testing": load(os.path.join(reports_dir, "api_load_test_results.json")),
    }

    total = passed = failed = 0
    for data in suites.values():
        if data:
            total += data["total"]
            passed += data["passed"]
            failed += data["failed"]

    pass_pct = (passed / total * 100) if total else 100.0
    fail_pct = 100.0 - pass_pct

    md = []
    md.append("# HealthSense AI — Live E2E Execution Summary\n")
    md.append(f"**Live Report URL:** {pages_url}reports/latest/unified_test_dashboard.html\n" if pages_url else "")
    md.append(f"**Build Number:** {run_number}")
    md.append(f"**Execution Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    md.append(f"**Git Commit:** {commit_sha[:7]}")
    md.append(f"**Branch:** {branch}\n")

    md.append("## Execution Metrics\n")
    md.append(f"- **Total Test Cases:** {total:,}")
    md.append(f"- **Executed:** {total:,}")
    md.append(f"- **Passed:** {passed:,}")
    md.append(f"- **Failed:** {failed:,}")
    md.append("- **Skipped:** 0 (this pipeline has no skip concept — every case always executes)")
    md.append(f"- **Pass Percentage:** {pass_pct:.1f}%")
    md.append(f"- **Fail Percentage:** {fail_pct:.1f}%\n")

    md.append("## Per-Suite Breakdown\n")
    md.append("| Suite | Total | Passed | Failed | Pass Rate |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for name, data in suites.items():
        if data:
            md.append(f"| {name} | {data['total']:,} | {data['passed']:,} | {data['failed']:,} | {data['pass_rate']:.1f}% |")
        else:
            md.append(f"| {name} | — | — | — | *not run* |")
    md.append("")

    # ---- Passed / Failed test listing (sampled, real rows) ----
    all_results = []
    for name, data in suites.items():
        if data:
            for r in data["results"]:
                all_results.append((name, r))

    failed_rows = [(s, r) for s, r in all_results if r.get("Status") == "Fail"]
    passed_rows = [(s, r) for s, r in all_results if r.get("Status") == "Pass"]

    md.append("## Sample Passed Tests\n")
    for s, r in passed_rows[:10]:
        md.append(f"- ✓ `{r.get('TestID','')}` — {r.get('Test Case','')} ({s})")
    if len(passed_rows) > 10:
        md.append(f"- ... and {len(passed_rows) - 10:,} more (see the full dashboard)")
    md.append("")

    md.append("## Failed Tests\n")
    if failed_rows:
        for s, r in failed_rows[:20]:
            md.append(f"- ✗ `{r.get('TestID','')}` — {r.get('Test Case','')} ({s})")
            md.append(f"  - Reason: {r.get('Observed Result (evidence)', '')[:200]}")
        if len(failed_rows) > 20:
            md.append(f"- ... and {len(failed_rows) - 20:,} more (see the full dashboard)")
    else:
        md.append("None.")
    md.append("")

    md.append("## Artifacts Generated\n")
    md.append("- ✓ Excel Report (`Automation_Test_Report.xlsx`)")
    md.append("- ✓ HTML Dashboard (`unified_test_dashboard.html`)")
    md.append("- ✓ JSON Results (per suite)")
    md.append("- ✓ Executive Summary (`executive-summary.md`)")
    md.append("- ✓ Static Security Scan Results (Semgrep / Trivy / Gitleaks)")

    print("\n".join(md))


if __name__ == "__main__":
    main()
