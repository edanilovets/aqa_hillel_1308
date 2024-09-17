import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(filename)s - %(lineno)d - %(funcName)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

logger.error('message ERROR')
logger.critical('message CRITICAL')