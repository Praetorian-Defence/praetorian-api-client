from dataclasses import dataclass
from uuid import UUID

from praetorian_api_client.resources.base import BaseResource


class LogResource(BaseResource):
    @dataclass
    class Log(object):
        id: UUID
        remote_id: UUID
        user_id: UUID
        device_id: UUID
        base_log: dict

    def create(self, remote_id: str, base_log: dict) -> Log:
        payload = self.fill_content(remote_id=remote_id, base_log=base_log)
        response = self.requestor.request('POST', 'logs/', payload=payload)['response']

        return self.Log(
            id=response.get('id'),
            remote_id=response.get('remote_id'),
            user_id=response.get('user_id'),
            device_id=response.get('device_id'),
            base_log=response.get('base_log'),
        )
