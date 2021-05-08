import uuid


class TestService:
    def test_successful_get_service(self, api_client):
        service = api_client.service.get(service_id='400469c6-8cd5-4c38-9add-b24bb637397b')

        assert hasattr(service, 'id') and uuid.UUID(service.id)

    def test_successful_list_services(self, api_client):
        service = api_client.service.list()

        assert isinstance(service, list) and hasattr(service[0], 'id') and uuid.UUID(service[0].id)

    def test_successful_list_services_filter(self, api_client):
        user = api_client.user.get_me()
        project = api_client.project.list(user_id=user.id)[0]
        remote = api_client.remote.list(project.id)[0]
        service = api_client.service.list(remote_id=remote.id, service_type='deploy')

        assert isinstance(service, list) and hasattr(service[0], 'id') and uuid.UUID(service[0].id)
