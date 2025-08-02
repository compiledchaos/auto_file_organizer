from organizer.logger_code import get_logger


def setup(args):
    if args.logfile:
        log = get_logger(log_to_file=True, log_file=args.logfile)
    else:
        log = get_logger()

    return log
