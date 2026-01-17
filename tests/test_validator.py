import pytest

from src.validator import validate_results, ValidationError

def valid_record():
    return {
        "test_id": "1",
        "test_name": "SampleTest",
        "status": "PASS",
        "duration_ms": 150
    }

def test_validate_success():
    records = [valid_record()]
    validated = validate_results(records)
    assert validated[0]["test_id"] == "1"
    assert validated[0]["duration_ms"] == 150
    assert validated[0]["status"] == "PASS"

def test_missing_required_field():
    record = valid_record()
    del record["test_name"]
    with pytest.raises(ValidationError):
        validate_results([record])

def test_invalid_status():
    record = valid_record()
    record["status"] = "UNKNOWN"
    with pytest.raises(ValidationError):
        validate_results([record])

def test_invalid_duration():
    record = valid_record()
    record["duration_ms"] = "abc"
    with pytest.raises(ValidationError):
        validate_results([record])

def test_results_not_list():
    with pytest.raises(ValidationError):
        validate_results("not_a_list")
