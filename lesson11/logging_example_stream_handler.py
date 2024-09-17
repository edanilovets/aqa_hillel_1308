import logging
import sys

# root
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(sys.stderr)
console_handler.setLevel(logging.CRITICAL)
# attach console_handler
logging.getLogger('').addHandler(console_handler)


# DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.debug('message from debug')
logging.info('message INFO')
logging.warning('message WARNING')
logging.error('message ERROR')
logging.critical('message CRITICAL')
