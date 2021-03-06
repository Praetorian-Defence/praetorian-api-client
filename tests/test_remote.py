import uuid


class TestRemote:
    def test_successful_get_remote(self, api_client):
        remote = api_client.remote.get(remote_id='9f7ae332-8e2d-41c5-b9e6-b6deef4f0ccb')

        assert hasattr(remote, 'id') and uuid.UUID(remote.id)

    def test_successful_list_remotes(self, api_client):
        remotes = api_client.remote.list()

        assert isinstance(remotes, list) and hasattr(remotes[0], 'id') and uuid.UUID(remotes[0].id)

    def test_successful_list_remotes_filter(self, api_client):
        user = api_client.user.get_me()
        project = api_client.project.list(user_id=user.id)[0]
        remotes = api_client.remote.list(project.id)

        assert isinstance(remotes, list) and hasattr(remotes[0], 'id') and uuid.UUID(remotes[0].id)
