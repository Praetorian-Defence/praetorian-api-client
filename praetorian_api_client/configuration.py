class Environment(object):
    def __init__(self, name: str, api_url: str, read_only: bool = True):
        self._name = name
        self._api_url = api_url
        self._read_only = read_only

    @property
    def name(self) -> str:
        return self._name

    @property
    def api_url(self) -> str:
        return self._api_url

    @property
    def read_only(self) -> bool:
        return self._read_only

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"{self._name} ({self._api_url})"


class Configuration(object):
    def __init__(
            self, environment: Environment,
            key: str,
            secret: str,
            timeout: int = 30,
            token: str = None
    ):
        self._environment = environment
        self._key = key
        self._secret = secret
        self._timeout = timeout
        self._token = token

    def set_token(self, token: str):
        self._token = token

    @property
    def environment(self) -> Environment:
        return self._environment

    @property
    def key(self) -> str:
        return self._key

    @property
    def secret(self) -> str:
        return self._secret

    @property
    def timeout(self) -> int:
        return self._timeout

    @property
    def token(self) -> str:
        return self._token
