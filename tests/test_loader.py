import json
import pytest
from pathlib import Path

from src.loader import load_results, UnsupportedFileTypeError, FileLoadError

def test_load_csv_success():
    results = load_results("data/sample_results.csv")
    assert isinstance(results, list)
    assert len(results) > 0
    assert "test_id" in results[0]
    assert "status" in results[0]

def test_file_not_found():
    with pytest.raises(FileLoadError):
        load_results("data/non_existent_file.csv")

def test_unsupported_file_type(tmp_path: Path):
    fake_file = tmp_path / "results.txt"
    fake_file.write_text("Invalid content")

    with pytest.raises(UnsupportedFileTypeError):
        load_results(str(fake_file))

def test_invalid_json(tmp_path: Path):
    invalid_json_file = tmp_path / "invalid_results.json"
    invalid_json_file.write_text("{invalid_json: true}")

    with pytest.raises(FileLoadError):
        load_results(str(invalid_json_file))

def test_valid_json(tmp_path: Path):
    data = [
        {
            "test_id": "1",
            "test_name": "SampleTest",
            "status": "PASS",
            "duration_ms": 100
        }
    ]
    valid_json_file = tmp_path / "valid_results.json"
    valid_json_file.write_text(json.dumps(data))

    results = load_results(str(valid_json_file))
    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0]["test_id"] == "1"
    assert results[0]["status"] == "PASS"
