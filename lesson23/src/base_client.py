import requests
import logging
import configparser

class BaseClient:

    BASE_URL = None

    def __init__(self, api_key: str = None, env="qa"):
        self.api_key = api_key
        self.logger = logging
        config = configparser.ConfigParser()
        config.read("/Users/danilovets/Personal/Hillel/aqa_hillel_1308/lesson23/settings.ini")
        if env in config:
            self.BASE_URL = config[env]["BASE_URL"]
        else:
            raise ValueError(f"Environment is not supported {env}")


    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        json = kwargs.get("json", {})
        headers = kwargs.get("headers", {})
        if self.api_key:
            headers["api_key"] = self.api_key
        kwargs["headers"] = headers

        self.logger.info(
            "Making %s a request to %s%s%s%s",
            method.upper(),
            url,
            f" with params {params}" if params else "",
            f" with params {data}" if data else "",
            f" with params {json}" if json else "",
        )
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.HTTPError as e:
            raise RuntimeError(f"HTTP error occurred {e}")
        except requests.RequestException as e:
            raise RuntimeError(f"RequestException error occurred {e}")
