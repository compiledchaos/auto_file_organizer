from organizer.app import run_gui
from commands import cli, args
import sys
from file_watchdog import activate_watchdog


if __name__ == "__main__":
    try:
        if args.gui:
            run_gui()
        else:
            if args.watchdog:
                activate_watchdog()
            cli()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)
