import pytest
from framework.utils.failure_analyzer import analyze_failure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        analyze_failure(item.name, str(report.longrepr))