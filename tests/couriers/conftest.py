import pytest
import requests
import random
import time

from data import MAIN_URL, LOGIN, PASSWORD, CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL, FIRST_NAME
from helpers import generate_login, generate_password


@pytest.fixture()
def delete_courier():
    yield
    # Получить id курьера
    payload = {"login": LOGIN, "password": PASSWORD}
    response = requests.post(f'{MAIN_URL}{LOGIN_COURIER_URL}', data=payload)
    # Проверяем, что запрос выполнен успешно и в ответе есть ключ 'id'
    if response.status_code == 200 and 'id' in response.json():
        id_courier = response.json()['id']
        # Удалить курьера
        delete_response = requests.delete(f'{MAIN_URL}{DELETE_COURIER_URL.format(id=id_courier)}')
        print(f"Курьер с id {id_courier} удален. Статус: {delete_response.status_code}")
    else:
        print(f"Ошибка: не удалось получить id курьера. Ответ сервера: {response.status_code}, {response.json()}")


@pytest.fixture()
def create_courier():
    # Создать нового курьера
    payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
    response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)
    # Проверяем, что курьер успешно создан
    if response.status_code == 201:
        print(f"Курьер с логином {LOGIN} создан. Ответ сервера: {response.json()}")
    else:
        print(f"Ошибка при создании курьера. Ответ сервера: {response.status_code}, {response.json()}")

    # Возвращаем данные курьера для использования в тестах
    yield {
        "login": LOGIN,
        "password": PASSWORD,
        "first_name": FIRST_NAME
    }