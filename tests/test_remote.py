import uuid


class TestRemote:
    def test_successful_list_remotes(self, api_client):
        user = api_client.user.get_me()
        project = api_client.project.list(user_id=user.id)[0]
        remotes = api_client.remote.list(project.id)

        assert isinstance(remotes, list) and hasattr(remotes[0], 'id') and uuid.UUID(remotes[0].id)
