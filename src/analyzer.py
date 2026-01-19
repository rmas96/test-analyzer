from typing import List, Dict

def analyze_results(results: List[Dict]) -> Dict:
    """Analyze test results and return summary metrics.
    
    Args
        results (List[Dict]): List of validated test result records.

    Returns:
        Dict: Summary metrics.
    """

    total = len(results)

    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    errors = sum(1 for r in results if r["status"] == "ERROR")

    total_duration = sum(r["duration_ms"] for r in results)
    average_duration = total_duration / total if total > 0 else 0

    failed_tests = [r for r in results if r["status"] != "PASS"]

    success_rate = (passed / total * 100) if total > 0 else 0

    summary = {
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "total_duration_ms": total_duration,
        "average_duration_ms": average_duration,
        "failed_tests": failed_tests,
        "success_rate_percent": success_rate
    }
    return summary