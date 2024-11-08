import logging

import requests


class BaseClient:

    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.config['base_url']}{endpoint}"
        params = kwargs.get("params", {})
        data = kwargs.get("data", {})
        json = kwargs.get("json", {})
        headers = kwargs.get("headers", {})
        api_key = self.config.get('api_key')
        if api_key:
            headers["api_key"] = api_key
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
