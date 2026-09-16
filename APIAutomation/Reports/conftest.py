import pytest
import os
import time
from datetime import datetime

# Global execution state telemetry tracking array matrices
passed_count = 0
failed_count = 0
skipped_count = 0
test_records = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Replaces Java TestNG ITestListener hooks (onTestStart, onTestSuccess, onTestFailure).
    """
    global passed_count, failed_count, skipped_count

    outcome = yield
    report = outcome.get_result()

    # Track lifecycle results exclusively during the functional execution phase
    if report.when == "call":
        test_name = item.name.replace("test_", "").replace("_", " ").title()
        duration = f"{report.duration:.2f}s"
        error_msg = "N/A - Completed Safely"

        if report.passed:
            passed_count += 1
            status = "PASSED"
            badge_class = "success"
        elif report.failed:
            failed_count += 1
            status = "FAIL"
            badge_class = "danger"
            error_msg = str(call.excinfo.value) if call.excinfo else "Unknown Execution Exception"
        else:
            skipped_count += 1
            status = "SKIPPED"
            badge_class = "warning"

        test_records.append({
            "name": test_name,
            "status": status,
            "badge": badge_class,
            "duration": duration,
            "error": error_msg
        })


def pytest_sessionfinish(session, exitstatus):
    """
    Replaces TestNG onFinish and extent.flush() to cleanly build the final report page.
    """
    total_tests = passed_count + failed_count + skipped_count
    if total_tests == 0:
        return

    # Calculate angular slice paths for the custom HTML/CSS responsive Pie Chart
    pass_deg = (passed_count / total_tests) * 360
    fail_deg = (failed_count / total_tests) * 360
    fail_bound = pass_deg + fail_deg

    # Generate the log metrics display rows grid block
    table_rows = "".join([f"""
        <tr>
            <td><strong>{t['name']}</strong></td>
            <td><span class="badge {t['badge']}">{t['status']}</span></td>
            <td>{t['duration']}</td>
            <td>{f'<div class="error-msg">{t["error"]}</div>' if t['status'] == 'FAIL' else f'<span style="color:#868e96;">{t["error"]}</span>'}</td>
        </tr>
    """ for t in test_records])

    # Replaces ExtentSparkReporter design layout using a self-contained dashboard layout template string
    html_report_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>UIBank API Automation Dashboard</title>
        <style>
            :root {{
                --bg-canvas: #f8f9fa; --bg-card: #ffffff; --text-main: #212529; --text-muted: #6c757d;
                --color-pass: #2b8a3e; --bg-pass: #d3f9d8; --color-fail: #c92a2a; --bg-fail: #ffe3e3; --border-ui: #dee2e6;
            }}
            body {{ font-family: system-ui, -apple-system, sans-serif; background: var(--bg-canvas); color: var(--text-main); margin: 0; padding: 40px 20px; }}
            .container {{ max-width: 1100px; margin: 0 auto; background: var(--bg-card); padding: 30px; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.05); }}
            header {{ border-bottom: 2px solid var(--border-ui); padding-bottom: 20px; margin-bottom: 30px; }}
            h1 {{ margin: 0; font-size: 1.8rem; color: #1c7ed6; }}
            .timestamp {{ font-size: 0.9rem; color: var(--text-muted); margin-top: 5px; }}
            .analytics-row {{ display: flex; gap: 40px; align-items: center; flex-wrap: wrap; margin-bottom: 40px; }}
            .pie-chart {{
                width: 200px; height: 200px; border-radius: 50%;
                background: conic-gradient(var(--color-pass) 0deg {pass_deg:.2f}deg, var(--color-fail) {pass_deg:.2f}deg {fail_bound:.2f}deg, #adb5bd {fail_bound:.2f}deg 360deg);
                box-shadow: inset 0 0 0 2px #fff, 0 4px 12px rgba(0,0,0,0.1);
            }}
            .info-box {{ flex: 1; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; }}
            .info-card {{ background: var(--bg-canvas); padding: 12px 18px; border-radius: 6px; border: 1px solid var(--border-ui); }}
            .info-card .label {{ font-size: 0.8rem; text-transform: uppercase; color: var(--text-muted); font-weight: 600; }}
            .info-card .value {{ font-size: 1.1rem; font-weight: 700; margin-top: 2px; }}
            .counts-row {{ display: flex; gap: 15px; margin-bottom: 30px; }}
            .count-item {{ flex: 1; padding: 15px; border-radius: 6px; text-align: center; background: var(--bg-canvas); border: 1px solid var(--border-ui); font-size: 1.1rem; font-weight: bold; }}
            .count-item.pass {{ border-left: 5px solid var(--color-pass); color: var(--color-pass); }}
            .count-item.fail {{ border-left: 5px solid var(--color-fail); color: var(--color-fail); }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid var(--border-ui); vertical-align: top; font-size: 0.95rem; }}
            th {{ background: var(--bg-canvas); font-weight: 600; }}
            .badge {{ display: inline-block; padding: 4px 8px; font-size: 0.8rem; font-weight: bold; border-radius: 4px; }}
            .badge.success {{ background: var(--bg-pass); color: var(--color-pass); }}
            .badge.danger {{ background: var(--bg-fail); color: var(--color-fail); }}
            .badge.warning {{ background: #e9ecef; color: #495057; }}
            .error-msg {{ font-family: monospace; font-size: 0.85rem; color: var(--color-fail); background: #fff5f5; padding: 8px; border-radius: 4px; border: 1px dashed #ffa8a8; margin-top: 5px; white-space: pre-wrap; }}
        </style>
    </head>
    <body>
    <div class="container">
        <header>
            <h1>📊 UIBank API Automation Dashboard</h1>
            <div class="timestamp">Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        </header>
        <section class="analytics-row">
            <div class="pie-chart"></div>
            <div class="info-box">
                <div class="info-card"><div class="label">Tester</div><div class="value">Sizwe Ngwenya</div></div>
                <div class="info-card"><div class="label">Framework</div><div class="value">Python pytest + Requests</div></div>
                <div class="info-card"><div class="label">Environment</div><div class="value">QA Back-End Gateway</div></div>
            </div>
        </section>
        <section class="counts-row">
            <div class="count-item">Total Run: {total_tests}</div>
            <div class="count-item pass">Passed: {passed_count}</div>
            <div class="count-item fail">Failed: {failed_count}</div>
            <div class="count-item">Skipped: {skipped_count}</div>
        </section>
        <section>
            <h2>API Execution Activity Logs</h2>
            <table>
                <thead><tr><th>Target Request Operation</th><th>Status</th><th>Duration</th><th>Response Diagnostics</th></tr></thead>
                <tbody>{table_rows}</tbody>
            </table>
        </section>
    </div>
    </body>
    </html>
    """

    report_dir = os.path.join(session.config.rootdir, "APIAutomation", "Reports")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, "API_Report.html")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_report_content)

    print(f"\n[EXTENT MANAGER] Extent Report Generated Successfully at: {report_path}")
