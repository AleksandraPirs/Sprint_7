import allure
import pytest
import requests
import logging
from helpers import generate_password, generate_login
from data import MAIN_URL, LOGIN, PASSWORD

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[logging.StreamHandler()]  # Вывод в консоль
)


class TestLoginCourier:

    @allure.title('Выполнить логин с логином и паролем')
    def test_login_courier_with_login_password_true(self, create_courier):
        payload = {"login": LOGIN, "password": PASSWORD}
        response = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на логин курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        id_courier = response.json()['id']
        assert response.status_code == 200 and response.json()['id'] == id_courier

    @allure.title('Выполнить логин с несуществующим логином и паролем')
    def test_login_courier_with_bad_login_password_return_message_error(self):
        payload = {"login": generate_login(), "password": generate_password()}
        response = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на логин курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Выполнить логин без логина или пароля')
    @pytest.mark.parametrize('login_courier, password_courier', [[generate_login(), ''], ['', generate_password()]])
    def test_login_courier_without_login_or_password_return_message_error(self, login_courier, password_courier):
        payload = {"login": login_courier, "password": password_courier}
        response = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на логин курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert response.status_code == 400 and response.json() == {'code': 400,
                                                                   'message': 'Недостаточно данных для входа'}

    @allure.title('Логин возвращает идентификатор курьера')
    def test_login_courier_return_id_courier(self, create_courier):
        payload = {"login": LOGIN, "password": PASSWORD}
        response = requests.post(f'{MAIN_URL}/api/v1/courier/login', data=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на логин курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        # Проверка статус кода и наличия id в ответе
        assert response.status_code == 200, f"Ожидался статус код 200, но получен {response.status_code}"
        assert 'id' in response.json(), "В ответе отсутствует ключ 'id'"
        id_courier = response.json()['id']
        assert response.json()['id'] == id_courier