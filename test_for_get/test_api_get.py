"""Тесты для запроса GET"""
import allure

from jsonschema import validate
from conftest import headers


def test_get_status_code(api_client, headers=headers):
    """Test for status code
    Args:
        api_client- фикстура API клиента
        headers- заголовки запроса
        """
    response = api_client.get(path="/api/movies", headers=headers)
    assert response.ok


def test_get_content_type(api_client, headers=headers):
    """Test check format
       Args:
        api_client- фикстура API клиента
        headers- заголовки запроса
        """
    response = api_client.get(path="/api/movies", headers=headers)
    assert response.headers['Content-Type'] == "application/json"


def test_get_json_schema(api_client, headers=headers):
    """Test validate schema of response
       Args:
        api_client- фикстура API клиента
        headers- заголовки запроса
        """
    response = api_client.get(path="/api/movies", headers=headers)
    schema = {}
    validate(instance=response.json(), schema=schema)


def test_get_response(api_client, headers=headers):
    """Test response
       Args:
        api_client- фикстура API клиента
        headers- заголовки запроса
        """
    response = api_client.get(path="/api/movies", headers=headers).json()
    assert response['items'] == []

