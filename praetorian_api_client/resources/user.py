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
        additional_data: dict

    @dataclass
    class TemporaryUser(object):
        username: str
        password: str

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
            is_temporary=response.get('is_temporary'),
            additional_data=response.get('additional_data')
        )

    def delete_me(self) -> bool:
        response = self.requestor.request('DELETE', f'users/me/', parse=False)
        is_deleted = False

        if response is not None:
            is_deleted = True

        return is_deleted

    def create_temporary(self, project_id: str, remote_id: str) -> TemporaryUser:
        payload = self.fill_content(project_id=project_id, remote_id=remote_id)
        response = self.requestor.request('POST', 'temporary_users/create/', payload=payload)['response']

        return self.TemporaryUser(
            username=response.get('username'),
            password=response.get('password')
        )
