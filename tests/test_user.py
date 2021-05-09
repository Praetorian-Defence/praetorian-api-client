import uuid

from praetorian_api_client.resources.user import UserResource


class TestUser:
    def test_successful_get_me(self, api_client):
        user = api_client.user.get_me()

        assert hasattr(user, 'id') and uuid.UUID(user.id)

    def test_successful_delete(self, api_client):
        is_deleted = api_client.user.delete_me()

        assert is_deleted

    def test_successful_create(self, api_client):
        remote_id = '9f7ae332-8e2d-41c5-b9e6-b6deef4f0ccb'
        project_id = '408c57f3-6ea4-42dc-beb3-a0051b97182f'

        temp_user = api_client.user.create_temporary(project_id=project_id, remote_id=remote_id)

        assert isinstance(temp_user, UserResource.TemporaryUser) \
               and hasattr(temp_user, 'username') \
               and hasattr(temp_user, 'password')
