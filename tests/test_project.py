import uuid


class TestProject:
    def test_successful_list_projects(self, api_client):
        user = api_client.user.get_me()
        projects = api_client.project.list(user_id=user.id)

        assert isinstance(projects, list) and hasattr(projects[0], 'id') and uuid.UUID(projects[0].id)
