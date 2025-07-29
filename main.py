from organizer.core import FileOrganizer
from cli import parse_args
from organizer.utils.data import history
import json
from pathlib import Path
from organizer.app import run

args = parse_args()


def main():
    source = args.source or str(Path.home() / "Downloads")
    rules = args.rules
    data = history
    simulate = args.simulate
    reset = args.reset

    with open(rules) as f:
        rules = json.load(f)

    organizer = FileOrganizer(source, rules, data, simulate)

    if args.undo:
        organizer.undo()
    if reset:
        organizer.reset()

    organizer.organize()


if __name__ == "__main__":
    if args.gui:
        run()
    else:
        main()
