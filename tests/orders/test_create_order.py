import allure
import requests
import logging
from helpers import generate_first_name, generate_password, generate_address, generate_metro_station, \
    generate_phone, generate_rent_time, generate_delivery_date, generate_comment, generate_color
from data import MAIN_URL, CREATE_ORDER_URL

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[logging.StreamHandler()]  # Вывод в консоль
)


class TestCreateOrder:

    @allure.title('Создать заказ самоката черного или серого цвета')
    def test_create_order_with_color_black_or_grey(self):
        # Создать заказ самоката с ЧЕРНЫМ ИЛИ СЕРЫМ цветом
        payload_order = {
            "firstName": generate_first_name(),
            "lastName": generate_password(),
            "address": generate_address(),
            "metroStation": generate_metro_station(),
            "phone": generate_phone(),
            "rentTime": generate_rent_time(),
            "deliveryDate": generate_delivery_date(),
            "comment": generate_comment(),
            "color": generate_color()
        }
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание заказа: {payload_order}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert response.status_code == 201

    @allure.title('Создать заказ самоката черного и серого цвета')
    def test_create_order_with_color_black_and_grey(self):
        # Создать заказ самоката с ЧЕРНЫМ И СЕРЫМ цветом
        payload_order = {
            "firstName": generate_first_name(),
            "lastName": generate_password(),
            "address": generate_address(),
            "metroStation": generate_metro_station(),
            "phone": generate_phone(),
            "rentTime": generate_rent_time(),
            "deliveryDate": generate_delivery_date(),
            "comment": generate_comment(),
            "color": ['BLACK', 'GREY']
        }
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание заказа: {payload_order}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert response.status_code == 201

    @allure.title('Создать заказ самоката без цвета')
    def test_create_order_without_color(self):
        # Создать заказ самоката без указания цвета
        payload_order = {
            "firstName": generate_first_name(),
            "lastName": generate_password(),
            "address": generate_address(),
            "metroStation": generate_metro_station(),
            "phone": generate_phone(),
            "rentTime": generate_rent_time(),
            "deliveryDate": generate_delivery_date(),
            "comment": generate_comment(),
            "color": ['']
        }
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание заказа: {payload_order}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert response.status_code == 201

    @allure.title('Создать заказ и получить номер заказа')
    def test_create_order_return_code_track_order(self):
        # Создать заказ самоката с ЧЕРНЫМ ИЛИ СЕРЫМ цветом
        payload_order = {
            "firstName": generate_first_name(),
            "lastName": generate_password(),
            "address": generate_address(),
            "metroStation": generate_metro_station(),
            "phone": generate_phone(),
            "rentTime": generate_rent_time(),
            "deliveryDate": generate_delivery_date(),
            "comment": generate_comment(),
            "color": generate_color()
        }
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        # Логирование запроса и ответа
        logging.info(f"Запрос на создание заказа: {payload_order}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert 'track' in response.json()