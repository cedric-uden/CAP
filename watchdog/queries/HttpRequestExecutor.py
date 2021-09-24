import watchdog.logs.Logging as log
import requests


class HttpRequestExecutor:

    _logger = log.get_logger(__name__)

    def post(self, url, **kwargs):

        data = kwargs.get("data")
        headers = kwargs.get("headers")
        params = kwargs.get("params")

        if data:
            self._logger.info(f"Posting to URL {url} "
                              f"with params {list(data.keys())}")

        if headers:
            self._logger.info(f"Posting to URL {url} "
                              f"with headers {list(headers.keys())}")

        if params:
            self._logger.info(f"Posting to URL {url} "
                              f"with params {list(params.keys())}")

        return requests.post(url, **kwargs)
