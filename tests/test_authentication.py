import uuid

import pytest

from praetorian_api_client.api_client import ApiClient
from praetorian_api_client.errors import ApiException


class TestAuthentication:
    def test_successful_authentication(self, api_client):
        assert hasattr(api_client.configuration, 'token') and uuid.UUID(api_client.configuration.token)

    def test_unsuccessful_authentication(self, configuration):
        with pytest.raises(
                ApiException, match='401 Client Error: Unauthorized for url: http://127.0.0.1:8000/v1/tokens/'
        ):
            ApiClient.create_from_auth(configuration, 'test@praetorian.sk', '1234')
