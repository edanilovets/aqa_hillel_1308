import requests
from lesson11.src.utils.logger_util import logger

base_url = 'http://127.0.0.1:7070'

def create_car_record(content):
    logger.info(f"Creating car record with {content}")
    response_data = requests.post(f'{base_url}/content', json=content)
    logger.info(f"Creating response {response_data.json()}")
    return response_data