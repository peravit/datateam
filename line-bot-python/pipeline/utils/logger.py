import logging

from .file import mkdir


def create_logger(name, format_type="txt"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    mkdir("_logs")
    fh = logging.FileHandler("_logs/{}.{}".format(name, format_type))
    fh.setLevel(logging.DEBUG)

    frmt = logging.Formatter("%(message)s")
    fh.setFormatter(frmt)
    logger.addHandler(fh)

    return logger
