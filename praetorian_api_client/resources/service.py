from dataclasses import dataclass
from typing import List
from uuid import UUID

from praetorian_api_client.resources.base import BaseResource


class ServiceResource(BaseResource):
    @dataclass
    class Service(object):
        id: UUID
        name: str
        type: str
        variables: dict

    def list(self, remote_id: str = None, name: str = None, service_type: str = None) -> List[Service]:
        query = self.fill_content(remote_id=remote_id, name=name, type=service_type)
        response = self.requestor.request('GET', 'services/', query=query)['items']

        return [
            self.Service(
                id=item.get('id'),
                name=item.get('name'),
                type=item.get('type'),
                variables=item.get('variables')
            ) for item in response
        ]

    def get(self, service_id: str) -> Service:
        response = self.requestor.request('GET', f'services/{service_id}/')['response']

        return self.Service(
            id=response.get('id'),
            name=response.get('name'),
            type=response.get('type'),
            variables=response.get('variables')
        )
