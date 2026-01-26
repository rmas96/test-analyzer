# Automated Test Result Analyzer

A small Python tool to load, validate, and analyze automated test results from CSV or JSON files.

## Features
- Supports CSV and JSON input
- Validates test result structure and values
- Computes useful metrics:
  - total tests
  - pass / fail / error counts
  - success rate
  - total and average duration
- Simple CLI interface
- Tested with pytest

## Project Structure
test-result-analyzer/
├─ src/
│   ├─ loader.py       # load CSV / JSON
│   ├─ validator.py    # validate schema
│   ├─ analyzer.py     # stats & classification
│   ├─ reporter.py     # text report (not implemented)
│   └─ main.py         # CLI entry point
└─ tests/
    ├─ test_loader.py
    ├─ test_validator.py
    └─ test_analyzer.py

## Usage
python src/main.py data/sample_results.csv

## Example Output
{
    "total_tests": 4,
    "passed": 2,
    "failed": 1,
    "errors": 1,
    "total_duration_ms": 710,
    "average_duration_ms": 177.5,
    "failed_tests": [
        {
            "test_id": "2",
            "test_name": "AudioOutputTest",
            "status": "FAIL",
            "duration_ms": 340,
            "error_message": "Output level below threshold"
        },
        {
            "test_id": "3",
            "test_name": "NetworkInit",
            "status": "ERROR",
            "duration_ms": 50,
            "error_message": "Timeout during initialization"
        }
    ],
    "success_rate_percent": 50.0
}

## Running Tests
pytest

## Requirements
Python 3.12.3
pytest
