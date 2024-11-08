from lesson24.src.pet_api import PetApi
from lesson24.src.store_api import StoreApi
from lesson24.src.user_api import UserApi
import configparser
from pathlib import Path

class App:
    def __init__(self, env="qa", api_key: str = None):
        config = configparser.ConfigParser()
        config_path = Path(__file__).resolve().parent.parent / "settings.ini"
        config.read(config_path)
        if env in config:
            base_url = config[env]["BASE_URL"]
        else:
            raise ValueError(f"Environment is not supported {env}")

        config = {section: dict(config[section]) for section in config.sections()}
        config["api_key"] = api_key
        config["base_url"] = base_url

        self.pet = PetApi(config)
        self.user = UserApi(config)
        self.store = StoreApi(config)