import csv
import json
from pathlib import Path

class UnsupportedFileTypeError(Exception):
    pass

class FileLoadError(Exception):
    pass

def load_results(file_path: str) -> list[dict]:
    """
    Load results from a file. Supports CSV and JSON formats.

    Args:
        file_path (str): The path to the file to load.
    Returns:
        list[dict]: A list of dictionaries representing the loaded results.
    Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        FileLoadError: If there is an error loading the file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileLoadError(f"File not found: {file_path}")

    if path.suffix.lower() == '.csv':
        return _load_csv(path)
    elif path.suffix.lower() == '.json':
        return _load_json(path)
    else:
        raise UnsupportedFileTypeError(f"Unsupported file type: {path.suffix}")
    
def _load_csv(path: Path) -> list[dict]:
    try:
        with path.open(newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except Exception as e:
        raise FileLoadError(f"Error loading CSV file: {e}") from e
    
def _load_json(path: Path) -> list[dict]:
    try:
        with path.open(encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

        if not isinstance(data, list):
            raise FileLoadError("JSON file does not contain a list of results.")
        
        return data
    except json.JSONDecodeError as e:
        raise FileLoadError(f"Invalid JSON format from{path}: {e}") from e
    except Exception as e:
        raise FileLoadError(f"Error loading JSON file from {path}: {e}") from e
