import uuid


class TestUser:
    def test_successful_get_me(self, api_client):
        user = api_client.user.get_me()

        assert hasattr(user, 'id') and uuid.UUID(user.id)

    def test_successful_delete(self, api_client):
        is_deleted = api_client.user.delete_me()

        assert is_deleted
