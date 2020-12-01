from dataclasses import dataclass
from uuid import UUID

from praetorian_api_client.resources.base import BaseResource


class UserResource(BaseResource):
    @dataclass
    class User(object):
        id: UUID
        username: str
        name: str
        surname: str
        email: str
        phone: str
        role: str
        is_temporary: bool

    def get_me(self) -> User:
        response = self.requestor.request('GET', 'users/me/')['response']

        return self.User(
            id=response.get('id'),
            username=response.get('username'),
            name=response.get('name'),
            surname=response.get('surname'),
            email=response.get('email'),
            phone=response.get('phone'),
            role=response.get('role'),
            is_temporary=response.get('is_temporary')
        )