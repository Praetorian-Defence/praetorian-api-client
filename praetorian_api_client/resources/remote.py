from dataclasses import dataclass
from typing import List
from uuid import UUID

from praetorian_api_client.resources.base import BaseResource


class RemoteResource(BaseResource):
    @dataclass
    class Remote(object):
        id: UUID
        name: str
        host: str
        port: str
        user: str
        password: str
        variables: dict
        project: dict

    def get(self, remote_id: str) -> Remote:
        response = self.requestor.request('GET', f'remotes/{remote_id}/')['response']

        return self.Remote(
            id=response.get('id'),
            name=response.get('name'),
            host=response.get('host'),
            port=response.get('port'),
            user=response.get('user'),
            password=response.get('password'),
            variables=response.get('variables'),
            project=response.get('project')
        )

    def list(self, project_id: str = None, name: str = None) -> List[Remote]:
        query = self.fill_content(project_id=project_id, name=name)
        response = self.requestor.request('GET', 'remotes/', query=query)['items']

        return [
            self.Remote(
                id=item.get('id'),
                name=item.get('name'),
                host=item.get('host'),
                port=item.get('port'),
                user=item.get('user'),
                password=item.get('password'),
                variables=item.get('variables'),
                project=item.get('project')
            ) for item in response
        ]
