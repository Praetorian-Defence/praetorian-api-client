from dataclasses import dataclass
from uuid import UUID

from praetorian_api_client.resources.base import BaseResource


class TokenResource(BaseResource):
    @dataclass
    class Token(object):
        token: UUID
        active_2fa: bool

    def auth(self, username: str, password: str) -> Token:
        payload = self.fill_content(username=username, password=password)
        response = self.requestor.request('POST', 'tokens/', payload=payload)['response']

        return self.Token(
            token=response.get('token'),
            active_2fa=response.get('active_2fa')
        )
