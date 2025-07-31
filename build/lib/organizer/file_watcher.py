import json
import time
from watchdog.observers import Observer
from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEventHandler
from pathlib import Path
from organizer.core import FileOrganizer
from organizer.utils.data import history
from organizer.args import args
from organizer.logger_code import get_logger


class MyHandler(FileSystemEventHandler):
    def __init__(self, organizer):
        super().__init__()
        self.organizer = organizer

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        self.organizer.organize()
        return super().on_created(event)


def activate_watchdog():

    if args.logfile:
        log = get_logger(log_to_file=True, log_file=args.logfile)
    else:
        log = get_logger()
    # Load rules from file if args.rules is a path
    if isinstance(args.rules, str) and Path(args.rules).is_file():
        with open(args.rules, "r", encoding="utf-8") as f:
            rules = json.load(f)
    else:
        rules = args.rules  # Already a dict

    organizer = FileOrganizer(args.source, rules, history, logger=log)
    path = Path(args.source)
    observer = Observer()
    handler = MyHandler(organizer)
    observer.schedule(handler, str(path), recursive=True)

    observer.start()

    try:
        log.info("Watching for changes. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Stopping observer...")
    finally:
        observer.stop()
        observer.join()
