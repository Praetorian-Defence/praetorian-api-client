import json
from typing import Union, Dict

from requests import Request, Session, RequestException, HTTPError

from .configuration import Configuration
from .errors import ApiException
from .utils import JSONEncoder
from . import version


class Requestor(object):
    def __init__(self, configuration: Configuration):
        self._user_agent = f"praetorian_api_client/{version.__version__}"
        self._configuration = configuration
        self._session = Session()

    def request(self, method: str, endpoint_url: str, payload: dict = None, query: dict = None, parse: bool = True) -> Union[str, Dict]:
        req = Request(
            method=method,
            url=self._configuration.environment.api_url + endpoint_url,
            headers={
                "User-Agent": self._user_agent,
                "X-ApiKey": self._configuration.key,
                "Authorization": f"TOKEN {self._configuration.token}",
            },
        )

        if payload and isinstance(payload, dict):
            req.data = json.dumps(payload, cls=JSONEncoder)
            req.headers['Content-Type'] = 'application/json'

        if query and isinstance(query, dict):
            req.params = query

        prepared = req.prepare()

        try:
            r = self._session.send(
                prepared,
                timeout=self._configuration.timeout
            )
        except RequestException:
            raise ApiException(prepared, 'Request to server timed out.')

        try:
            r.raise_for_status()
        except HTTPError as e:
            raise ApiException(prepared, e.args[0], previous=e)

        data = r.text

        if parse:
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise ApiException(prepared, 'Cannot parse response data to json.')

        return data

    def __str__(self) -> str:
        return self._user_agent
