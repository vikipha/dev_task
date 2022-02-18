import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_index(api_client: APIClient) -> None:
    response = api_client.get("/")
    assert response.status_code == 200
    assert b"database is configured properly" in response.content
