from dataclasses import dataclass
from typing import List
from uuid import UUID

from praetorian_api_client.resources.base import BaseResource


class ProjectResource(BaseResource):
    @dataclass
    class Project(object):
        id: UUID
        name: str
        is_vpn: bool

    def list(self, user_id: str = None, name: str = None) -> List[Project]:
        query = self.fill_content(user_id=user_id, name=name)
        response = self.requestor.request('GET', 'projects/', query=query)['items']

        return [
            self.Project(
                id=item.get('id'),
                name=item.get('name'),
                is_vpn=item.get('is_vpn')
            ) for item in response
        ]
