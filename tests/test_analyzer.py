import pytest
from src.analyzer import analyze_results

def sample_results():
    return [
        {
            "test_id": "1",
            "test_name": "BootTest",
            "status": "PASS",
            "duration_ms": 100,
        },
        {
            "test_id": "2",
            "test_name": "SensorTest",
            "status": "FAIL",
            "duration_ms": 200,
        },
        {
            "test_id": "3",
            "test_name": "CommsTest",
            "status": "ERROR",
            "duration_ms": 300,
        },
    ]

def test_analyze_basic_metrics():
    results = sample_results()
    summary = analyze_results(results)

    assert summary["total_tests"] == 3
    assert summary["passed"] == 1
    assert summary["failed"] == 1
    assert summary["errors"] == 1
    assert summary["total_duration_ms"] == 600
    assert summary["average_duration_ms"] == 200
    assert summary["success_rate_percent"] == pytest.approx(33.33, 0.1)

def test_analyze_failed_tests_details():
    results = sample_results()
    summary = analyze_results(results)

    failed_tests = summary["failed_tests"]
    assert len(failed_tests) == 2
    assert all(test["status"] != "PASS" for test in failed_tests)