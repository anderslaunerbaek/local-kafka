"""
Example for development:
log_level = logging.DEBUG

For production you rather want:
log_level = logging.WARNING
"""

import logging


def get_logger(name: str = "my-app", log_level: int = logging.DEBUG):
    """_summary_

    Args:
        name (str, optional): _description_. Defaults to "my-app".
        log_level (int, optional): _description_. Defaults to logging.NOTSET.

    Returns:
        _type_: _description_
    """
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        level=logging.NOTSET,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    return logger
