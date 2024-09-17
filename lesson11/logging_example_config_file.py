import logging
import logging.config

logging.config.fileConfig('logging_config.ini')
logger1 = logging.getLogger('sampleLogger')

logger1.debug('message DEBUG')
logger1.info('message INFO')
logger1.warning('message WARNING')
logger1.error('message ERROR')
logger1.critical('message CRITICAL')
