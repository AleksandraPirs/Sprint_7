import pytest
import requests
import logging
from data import MAIN_URL, CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL
from helpers import generate_login, generate_password, generate_first_name

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

@pytest.fixture()
def create_courier():
    """
    Фикстура для создания курьера перед выполнением теста.
    """
    # Генерация уникальных данных
    unique_login = generate_login()
    unique_password = generate_password()
    unique_first_name = generate_first_name()

    # Создать нового курьера
    payload = {
        "login": unique_login,
        "password": unique_password,
        "firstName": unique_first_name
    }
    response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

    # Проверяем, что курьер успешно создан
    if response.status_code == 201:
        logging.info(f"Курьер с логином {unique_login} создан. Ответ сервера: {response.json()}")
    else:
        logging.error(f"Ошибка при создании курьера. Ответ сервера: {response.status_code}, {response.json()}")

    # Возвращаем данные курьера для использования в тестах
    yield {
        "login": unique_login,
        "password": unique_password,
        "first_name": unique_first_name
    }

@pytest.fixture()
def delete_courier(create_courier):
    """
    Фикстура для удаления курьера после выполнения теста.
    """
    yield
    # Получить id курьера
    payload = {
        "login": create_courier["login"],
        "password": create_courier["password"]
    }
    response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', json=payload)

    # Проверяем, что запрос выполнен успешно и в ответе есть ключ 'id'
    if response.status_code == 200 and 'id' in response.json():
        id_courier = response.json()['id']
        # Удалить курьера
        delete_response = requests.delete(f'{MAIN_URL}{DELETE_COURIER_URL.format(id=id_courier)}')
        logging.info(f"Курьер с id {id_courier} удален. Статус: {delete_response.status_code}")
    else:
        logging.error(f"Ошибка: не удалось получить id курьера. Ответ сервера: {response.status_code}, {response.json()}")