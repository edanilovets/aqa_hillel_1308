import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(filename)s - %(lineno)d - %(funcName)s',
                    handlers=[
                        logging.StreamHandler(),  # log in console
                        logging.FileHandler('basic_example.log')  # in file
                    ])

logger = logging.getLogger(__name__)
