# praetorian-api-client

My name is Aurelius and I am emperor's counselor 👨‍⚖️. My everyday job is to maintain and manage communication 🗣 between praetorian 
Cornelius 🛡️ and military commander Maximus ⚔️.

Or just for normal people without abstract thinking I am API Client for praetorian-api project.

## Introduction

Praetorian API Client is used for creating requests to Praetorian API and for receiving responses which are deserialized to objects.

## Installation

```python
# pip
pip install praetorian-api-client

# pipenv
pipenv install praetorian-api-client

# poetry
poetry add praetorian-api-client
```

## Example

#### 1. Create Environment object

```python
from praetorian_api_client.configuration import Environment

environment = Environment(name='praetorian-api', api_url='http://127.0.0.1:8000/', read_only=False)
```

---

#### 2. Create Configuration object

```python
from praetorian_api_client.configuration import Configuration

configuration = Configuration(environment=environment, key='api-key', secret='api-secret')
```

#### 3. Create ApiClient object

```python
from praetorian_api_client.api_client import ApiClient

api_client = ApiClient.create_from_auth(configuration=configuration, username='username', password='password')
```

#### 3. Create request from ApiClient to Api

> This request will return (if successful) list of Remote objects.

```python
remotes = api_client.remote.list()
```

## Tests

To run tests, you need to run command: `pytest`

Tests require access data to the api. For security reasons, access data is stored in environment variables. To set 
environment variables, you need to create an `.env` file from the example in the `.env.example` file.

---
Developed with 💙 and ☕️ by [Adam Žúrek](https://zurek11.github.io/) & Erik Belák
with the support of [BACKBONE s.r.o.](https://www.backbone.sk/), 2024 (C)
