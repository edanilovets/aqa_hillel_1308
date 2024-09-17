import logging

logger = logging.getLogger("sampleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('log_file.txt')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.debug('message DEBUG')
logger.info('message INFO')
logger.warning('message WARNING')
logger.error('message ERROR')
logger.critical('message CRITICAL')
