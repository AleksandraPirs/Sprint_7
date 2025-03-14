import allure
import requests
from helpers import generate_password, generate_first_name
from data import MAIN_URL, LOGIN, PASSWORD, FIRST_NAME, CREATE_COURIER_URL


class TestCreateCourier:

    @allure.title('Создать двух одинаковых курьеров')
    def test_create_two_same_courier_show_message_conflict(self, create_courier, delete_courier):
        # Создать еще одного такого же курьера
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. Попробуйте другой."}

    @allure.title('Создать курьера и получить статус код 201')
    def test_create_courier_return_status_code_201(self, delete_courier):
        # Создать нового курьера
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 201

    @allure.title('Создать курьера и получить ответ от сервера ok: True')
    def test_create_courier_return_message_ok_true(self, delete_courier):
        # Создать нового курьера
        payload = {"login": LOGIN, "password": PASSWORD, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.json() == {"ok": True}

    @allure.title('Создать курьера без логина или пароля')
    def test_create_courier_without_required_field_show_message_bad_request(self):
        # Создать нового курьера без логина или пароля
        payload = {"login": LOGIN, "firstName": FIRST_NAME}
        response = requests.post(f'{MAIN_URL}{CREATE_COURIER_URL}', data=payload)

        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Создать курьера c логином, который уже существует в системе')
    def test_create_courier_with_login_already_exists_show_message_conflict(self, create_courier, delete_courier):
        # Создать еще одного курьера с таким же логином
        payload = {"login": LOGIN, "password": generate_password(), "firstName": generate_first_name()}
        response = requests.post(f'{MAIN_URL}/api/v1/courier', data=payload)

        assert response.status_code == 409 and response.json() == {"code": 409,
                                                                   "message": "Этот логин уже используется. Попробуйте другой."}