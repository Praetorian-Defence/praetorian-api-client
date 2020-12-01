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

    def list(self, project_id: str = None, name: str = None) -> List[Remote]:
        query = {}

        if project_id:
            query = query.update({'project_id': project_id})
        if name:
            query = query.update({'name': name})

        response = self.requestor.request('GET', 'remotes/', query=query)['items']

        return [
            self.Remote(
                id=item.get('id'),
                name=item.get('name'),
                host=item.get('host'),
                port=item.get('port')
            ) for item in response
        ]
