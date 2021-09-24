import watchdog.logs.Logging as log
import requests
from enum import Enum


class HttpValidQueries(Enum):
    POST = "POST"
    GET = "GET"


class HttpRequestExecutor:

    _logger = log.get_logger(__name__)

    def execute(self, url, method, **kwargs):
        data = kwargs.get("data")
        headers = kwargs.get("headers")
        params = kwargs.get("params")

        if data:
            self._logger.info(f"{method} to URL {url} "
                              f"with params {list(data.keys())}")

        if headers:
            self._logger.info(f"{method} to URL {url} "
                              f"with headers {list(headers.keys())}")

        if params:
            self._logger.info(f"{method} to URL {url} "
                              f"with params {list(params.keys())}")

        if method == HttpValidQueries.POST:
            return requests.post(url, **kwargs)
        elif method == HttpValidQueries.GET:
            return requests.get(url, **kwargs)

    def http_post(self, url, **kwargs):
        return self.execute(url, HttpValidQueries.POST, **kwargs)

    def http_get(self, url, **kwargs):
        return self.execute(url, HttpValidQueries.GET, **kwargs)
