# import logging
#
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# # DEBUG, INFO, WARNING, ERROR, CRITICAL
# logging.debug('message DEBUG')
# logging.info('message INFO')
# logging.warning('message WARNING')
# logging.error('message ERROR')
# logging.critical('message CRITICAL')

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # log in console
                        logging.FileHandler('basic_example.log')  # in file
                    ])

logger = logging.getLogger(__name__)

logger.error('message ERROR')
logger.critical('message CRITICAL')
