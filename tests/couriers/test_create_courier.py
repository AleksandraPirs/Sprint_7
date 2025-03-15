import allure
import requests
import logging
from helpers import generate_password, generate_first_name
from data import MAIN_URL, CREATE_COURIER_URL

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[logging.StreamHandler()]  # Вывод в консоль
)


class TestCreateCourier:

    @allure.title('Создать двух одинаковых курьеров')
    def test_create_two_same_courier_show_message_conflict(self, create_courier, delete_courier):
        # Создать еще одного такого же курьера
        payload = {
            "login": create_courier["login"],
            "password": create_courier["password"],
            "firstName": create_courier["first_name"]
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        # Проверка статус кода и тела ответа
        assert response.status_code == 409, f"Ожидался статус код 409, но получен {response.status_code}"
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }, f"Ожидался ответ {{'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}}, но получен {response.json()}"

    @allure.title('Создать курьера и получить статус код 201')
    def test_create_courier_return_status_code_201(self, create_courier, delete_courier):
        # Создать нового курьера
        payload = {
            "login": create_courier["login"],
            "password": create_courier["password"],
            "firstName": create_courier["first_name"]
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        # Проверка статус кода и тела ответа
        assert response.status_code == 201, f"Ожидался статус код 201, но получен {response.status_code}"
        assert response.json() == {"ok": True}, f"Ожидался ответ {{'ok': True}}, но получен {response.json()}"

    @allure.title('Создать курьера и получить ответ от сервера ok: True')
    def test_create_courier_return_message_ok_true(self, create_courier, delete_courier):
        # Создать нового курьера
        payload = {
            "login": create_courier["login"],
            "password": create_courier["password"],
            "firstName": create_courier["first_name"]
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        # Проверка статус кода и тела ответа
        assert response.status_code == 201, f"Ожидался статус код 201, но получен {response.status_code}"
        assert response.json() == {"ok": True}, f"Ожидался ответ {{'ok': True}}, но получен {response.json()}"

    @allure.title('Создать курьера без логина или пароля')
    def test_create_courier_without_required_field_show_message_bad_request(self):
        # Создать нового курьера без логина или пароля
        payload = {
            "login": "",  # Пустой логин
            "password": "",  # Пустой пароль
            "firstName": generate_first_name()  # Генерация имени
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        # Проверка статус кода и тела ответа
        assert response.status_code == 400, f"Ожидался статус код 400, но получен {response.status_code}"
        assert response.json() == {
            'code': 400,
            'message': 'Недостаточно данных для создания учетной записи'
        }, f"Ожидался ответ {{'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}}, но получен {response.json()}"

    @allure.title('Создать курьера c логином, который уже существует в системе')
    def test_create_courier_with_login_already_exists_show_message_conflict(self, create_courier, delete_courier):
        # Создать еще одного курьера с таким же логином
        payload = {
            "login": create_courier["login"],  # Используем логин из фикстуры
            "password": generate_password(),  # Генерация нового пароля
            "firstName": generate_first_name()  # Генерация нового имени
        }
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', json=payload)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание курьера: {payload}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        # Проверка статус кода и тела ответа
        assert response.status_code == 409, f"Ожидался статус код 409, но получен {response.status_code}"
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }, f"Ожидался ответ {{'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}}, но получен {response.json()}"