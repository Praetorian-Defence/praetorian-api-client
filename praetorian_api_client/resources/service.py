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

    def list(self, remote_id: str = None, service_type: str = None) -> List[Service]:
        query = {}

        if remote_id:
            query = query.update({'remote_id': remote_id})
        if service_type:
            query = query.update({'type': service_type})

        response = self.requestor.request('GET', 'services/', query=query)['items']

        return [
            self.Service(
                id=item.get('id'),
                name=item.get('name'),
                type=item.get('host'),
                variables=item.get('port')
            ) for item in response
        ]
