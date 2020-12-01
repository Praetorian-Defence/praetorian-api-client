import os
import pytest

from dotenv import load_dotenv

from praetorian_api_client.api_client import ApiClient
from praetorian_api_client.configuration import Environment, Configuration


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(BASE_DIR, '.env')

if os.path.exists(ENV_FILE):
    load_dotenv(dotenv_path=ENV_FILE, verbose=True)


@pytest.fixture(scope="module")
def configuration():
    environment = Environment(os.getenv('API_NAME'), os.getenv('API_URL'), read_only=False)
    return Configuration(environment, os.getenv('API_KEY'), os.getenv('API_SECRET'))


@pytest.fixture(scope="module")
def api_client(configuration):
    return ApiClient.create_from_auth(configuration, os.getenv('API_USERNAME'), os.getenv('API_PASSWORD'))
