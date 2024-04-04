from .resources.log import LogResource
from .resources.project import ProjectResource
from .resources.remote import RemoteResource
from .resources.service import ServiceResource
from .resources.token import TokenResource
from .resources.user import UserResource
from .version import __version__

from .configuration import Configuration
from .requestor import Requestor


class ApiClient(object):
    def __init__(self, configuration: Configuration):
        self._configuration = configuration
        self._requestor = Requestor(configuration)

        self._user = UserResource(self._requestor, self._configuration)
        self._project = ProjectResource(self._requestor, self._configuration)
        self._remote = RemoteResource(self._requestor, self._configuration)
        self._service = ServiceResource(self._requestor, self._configuration)
        self._log = LogResource(self._requestor, self._configuration)

    @classmethod
    def create_from_auth(cls, configuration: Configuration, username: str, password: str) -> 'ApiClient':
        token_resource = TokenResource(Requestor(configuration), configuration)
        token_obj = token_resource.auth(username, password)
        configuration.set_token(str(token_obj.token))

        return ApiClient(configuration)

    @property
    def version(self) -> str:
        return __version__

    @property
    def requestor(self) -> Requestor:
        return self._requestor

    @property
    def configuration(self) -> Configuration:
        return self._configuration

    @property
    def user(self) -> UserResource:
        return self._user

    @property
    def project(self) -> ProjectResource:
        return self._project

    @property
    def remote(self) -> RemoteResource:
        return self._remote

    @property
    def service(self) -> ServiceResource:
        return self._service

    @property
    def log(self) -> LogResource:
        return self._log

    def __str__(self) -> str:
        return f"{self.requestor}"
