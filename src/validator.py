from typing import List, Dict

class ValidationError(Exception):
    pass

REQUIRED_FIELDS = {"test_id",
                   "test_name",
                   "status",
                   "duration_ms"}

ALLOWED_STATUSES = {"PASS", "FAIL", "ERROR"}

def validate_results(results: List[Dict]) -> List[Dict]:
    """
    Validate a list of test results.

    Args:
        results (List[Dict]): Raw test results.
    Returns:
        List[Dict]: The validated and normalized test results.
    Raises:
        ValidationError: If validation fails.
    """

    if not isinstance(results, list):
        raise ValidationError("Results must be a list of records.")
    
    validated = []

    for index, record in enumerate(results):
        if not isinstance(record, dict):
            raise ValidationError(f"Record at index {index} is not a dictionary.")
        _validate_required_fields(record, index)
        _validate_status(record, index)
        _validate_duration(record, index)

        validated.append(record)

    return validated

def _validate_required_fields(record: Dict, index: int) -> None:
    missing_fields = REQUIRED_FIELDS - record.keys()
    if missing_fields:
        raise ValidationError(f"Record at index {index} is missing required fields: {missing_fields}")
    
def _validate_status(record: Dict, index: int) -> None:
    status = record.get("status")
    if status not in ALLOWED_STATUSES:
        raise ValidationError(f"Record at index {index} has invalid status: {status}"
                              f". Allowed statuses are: {ALLOWED_STATUSES}")

def _validate_duration(record: Dict, index: int) -> None:
    try:
        record["duration_ms"] = int(record["duration_ms"])
    except (ValueError, TypeError):
        raise ValidationError(f"Record at index {index} has invalid duration_ms: {record['duration_ms']}. It must be an integer.")
    