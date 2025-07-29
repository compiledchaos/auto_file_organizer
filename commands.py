from organizer.core import FileOrganizer
from cli import parse_args
from organizer.utils.data import history
import json
from pathlib import Path
import sys

args = parse_args()


def cli():
    source = args.source or str(Path.home() / "Downloads")
    rules_path = args.rules
    data = history
    simulate = args.simulate
    reset = args.reset

    # Error proofing for rules file
    try:
        with open(rules_path) as f:
            rules = json.load(f)
            if not isinstance(rules, dict):
                print(f"Rules file '{rules_path}' is not a valid JSON object.")
                sys.exit(1)
    except FileNotFoundError:
        print(f"Rules file '{rules_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from rules file '{rules_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error reading rules file '{rules_path}': {e}")
        sys.exit(1)

    try:
        organizer = FileOrganizer(source, rules, data, simulate)
    except Exception as e:
        print(f"Error initializing FileOrganizer: {e}")
        sys.exit(1)

    try:
        if args.undo:
            organizer.undo()
        if reset:
            organizer.reset()
        organizer.organize()
    except Exception as e:
        print(f"Error during organization: {e}")
