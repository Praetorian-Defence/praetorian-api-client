import hashlib
import hmac
from abc import ABC

from praetorian_api_client.configuration import Configuration
from praetorian_api_client.requestor import Requestor


class BaseResource(ABC):
    def __init__(self, requestor: Requestor, configuration: Configuration):
        self._requestor = requestor
        self._configuration = configuration

    def _sign(self, data: str) -> str:
        return hmac.new(self._configuration.secret.encode(), data.encode(), hashlib.sha256).hexdigest().upper()

    @staticmethod
    def fill_content(**kwargs) -> dict:
        values = {}
        for k in kwargs:
            if kwargs[k] is not None:
                values[k] = kwargs[k]
        return values

    @property
    def requestor(self) -> Requestor:
        return self._requestor

    @property
    def configuration(self) -> Configuration:
        return self._configuration
