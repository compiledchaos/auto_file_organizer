import json
import time
from watchdog.observers import Observer
from watchdog.events import DirCreatedEvent, FileCreatedEvent, FileSystemEventHandler
from pathlib import Path
from organizer.core import FileOrganizer
from organizer.utils.data import history
from organizer.logger_code import get_logger
from organizer.utils.data import rules_func


class MyHandler(FileSystemEventHandler):
    def __init__(self, organizer):
        super().__init__()
        self.organizer = organizer
        self.last_organize_time = 0
        self.organize_cooldown = 2  # Seconds to wait between organizes

    def _should_organize(self):
        """Check if enough time has passed since last organize to avoid spam"""
        import time

        current_time = time.time()
        if current_time - self.last_organize_time >= self.organize_cooldown:
            self.last_organize_time = current_time
            return True
        return False

    def on_created(self, event):
        """Handle file/directory creation events"""
        if not event.is_directory and self._should_organize():
            self.organizer.organize()
        return super().on_created(event)

    def on_moved(self, event):
        """Handle file/directory move events (common for browser downloads)"""
        if not event.is_directory and self._should_organize():
            self.organizer.organize()
        return super().on_moved(event)

    def on_modified(self, event):
        """Handle file modification events (for files that are written incrementally)"""
        if not event.is_directory and self._should_organize():
            # Only organize if the file is likely finished downloading
            # (this helps with large files that are written incrementally)
            import os
            import time

            try:
                # Check if file exists and is not being written to
                if hasattr(event, "src_path") and os.path.exists(event.src_path):
                    # Simple heuristic: if file size hasn't changed in 1 second, it's probably done
                    time.sleep(1)
                    if os.path.exists(event.src_path):
                        self.organizer.organize()
            except (OSError, AttributeError):
                # If we can't check the file, just organize anyway
                self.organizer.organize()


def activate_watchdog(args):
    """
    Activates a watchdog observer to monitor a specified directory for file changes.

    Args:
        args: Parsed command line arguments containing options for source directory,
              rules, logging, and more.

    The function initializes a logger based on the specified logging options. It loads
    file organization rules from a JSON file if a file path is provided in args.rules,
    otherwise it assumes args.rules is already a dictionary. It then creates a
    FileOrganizer instance with the specified source directory, rules, and history data.
    A watchdog observer is set up to monitor the source directory for changes, using a
    custom event handler to trigger file organization. The observer runs indefinitely
    until interrupted with a keyboard signal (Ctrl+C), at which point it stops and
    cleans up.
    """
    if args.logfile:
        log = get_logger(log_to_file=True, log_file=args.logfile)
    else:
        log = get_logger()
    # Load rules from file if args.rules is a path
    if isinstance(args.rules, str) and Path(args.rules).is_file():
        with open(args.rules, "r", encoding="utf-8") as f:
            rules = json.load(f)
    elif args.rules:
        rules = args.rules  # Already a dict
    else:
        rules = rules_func()
    history_data = history()
    organizer = FileOrganizer(args.source, rules, history_data, logger=log)
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
