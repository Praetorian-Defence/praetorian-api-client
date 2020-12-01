import pytest

from praetorian_api_client.api_client import ApiClient
from praetorian_api_client.configuration import Environment, Configuration
from praetorian_api_client.errors import ApiException


class TestConnection:
    def test_timed_out_server(self):
        environment = Environment('testing_api', 'http://127.0.0.1:1234/', read_only=False)
        configuration = Configuration(environment, 'key', 'secret')

        with pytest.raises(ApiException, match='Request to server timed out.'):
            ApiClient.create_from_auth(configuration, 'test', 'test')
