import logging
import uuid

process_uuid = str(uuid.uuid4())


CRITICAL = logging.CRITICAL
ERROR = logging.ERROR
WARNING = logging.WARNING
INFO = logging.INFO
DEBUG = logging.DEBUG


project_prefix = 'cap'


def get_logger(name):
    return logging.getLogger(f"{project_prefix}.{name}")


def setup(stream_level=logging.WARNING, file_level=logging.DEBUG, file_postfix=''):
    logger = logging.getLogger(project_prefix)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(project_prefix + file_postfix + '.log')
    fh.setLevel(file_level)

    ch = logging.StreamHandler()
    ch.setLevel(stream_level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        f'%(asctime)s - {process_uuid} - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
