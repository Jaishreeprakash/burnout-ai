"""Shared helpers for starting/waiting-on the real FastAPI backend used by
the test suites in this scripts/ folder. Every suite that needs a live
backend (functional/security tests, load tests) uses the same spawn logic
so behavior (SQLite DB, disabled OpenAI key) is consistent across suites."""
import os
import subprocess
import sys
import time

import httpx

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(REPO_ROOT, "backend")


def wait_for_health(base_url, timeout=45):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = httpx.get(f"{base_url}/health", timeout=2.0)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


def spawn_server(base_url, db_filename="backend_ci_test.db", workers=1):
    port = base_url.rsplit(":", 1)[-1]
    env = os.environ.copy()
    env["DATABASE_URL"] = f"sqlite:///./{db_filename}"
    env["OPENAI_API_KEY"] = ""  # deterministic smart-engine fallback, no upstream network calls
    db_path = os.path.join(BACKEND_DIR, db_filename)
    if os.path.exists(db_path):
        os.remove(db_path)
    cmd = [sys.executable, "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", port]
    if workers > 1:
        # Every route handler here is a synchronous `def`, so a single uvicorn
        # worker only has ~40 threadpool slots for concurrent requests — under
        # real concurrent load (see run_load_test.py) that queues and times
        # out well before 100 concurrent users. Multiple worker processes is
        # the standard fix and is required for a meaningful load-test result.
        cmd += ["--workers", str(workers)]
    proc = subprocess.Popen(
        cmd, cwd=BACKEND_DIR, env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return proc


def ensure_server(base_url, no_spawn, db_filename="backend_ci_test.db", workers=1):
    """Returns (proc_or_None, started_here_bool). Exits the process on failure."""
    if not no_spawn and not wait_for_health(base_url, timeout=1.5):
        print(f"No backend detected at {base_url} — starting uvicorn locally (SQLite, OpenAI disabled, {workers} worker(s))...")
        proc = spawn_server(base_url, db_filename, workers=workers)
        if not wait_for_health(base_url, timeout=45):
            proc.terminate()
            print("Backend failed to start within 45s.")
            sys.exit(1)
        print("Backend is up.")
        return proc, True
    elif not wait_for_health(base_url, timeout=5):
        print(f"No backend reachable at {base_url} and --no-spawn was set. Aborting.")
        sys.exit(1)
    return None, False


def teardown_server(proc, started_here, db_filename="backend_ci_test.db"):
    if started_here and proc:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except Exception:
            proc.kill()
        # With --workers > 1, uvicorn's child worker processes can hold the
        # SQLite file open for a moment after the parent process exits
        # (especially on Windows) — retry briefly rather than crash on cleanup.
        db_path = os.path.join(BACKEND_DIR, db_filename)
        for attempt in range(5):
            if not os.path.exists(db_path):
                break
            try:
                os.remove(db_path)
                break
            except OSError:
                time.sleep(1)
