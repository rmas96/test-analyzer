import sys
import json

from src.loader import load_results
from src.validator import validate_results
from src.analyzer import analyze_results

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <results_file>")
        sys.exit(1)

    results_file = sys.argv[1]

    try:
        raw_results = load_results(results_file)
        validated_result = validate_results(raw_results)
        summary = analyze_results(validated_result)

        print(json.dumps(summary, indent=4))

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()