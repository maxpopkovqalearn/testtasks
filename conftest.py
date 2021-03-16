"""Фикстуры для выбора необходимого линка, через коммандную строку"""
import pytest
import requests
import allure

#Сохранил токен отдельно, т.к. не было задачи проверять Post на получение токена.
#Возможно реализовать через преднастройку: создание устроиства и получение для него токена.
#Или один раз получить
headers={"X-TOKEN": "4dac2a92-08e2-4d31-abee-463d0545cf41"}

class APIClient:
    """Клиент для работы с API.
    Анализирует выбранный линк куда посылать запросы"""

    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        """Метод для POST"""
        url = self.base_address + path
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path=None, params=None, headers= None):
        """Метод для GET"""
        url = self.base_address + path
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)


@pytest.fixture(scope='session')
def api_client(request):
    """Фикстура для клиента"""
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)


def pytest_addoption(parser):
    """Парсер для выбора целевого линка до старта теста"""
    parser.addoption('--url',
                     action='store',
                     default='http://qa-test.iptv.rt.ru:4000',
                     help='Target link for request')

