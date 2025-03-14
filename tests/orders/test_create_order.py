import allure
import requests

from helpers import generate_first_name, generate_password, generate_address, generate_metro_station, \
    generate_phone, generate_rent_time, generate_delivery_date, generate_comment, generate_color
from data import MAIN_URL, CREATE_ORDER_URL


class TestCreateOrder:

    @allure.title('Создать заказ самоката черного или серого цвета')
    def test_create_order_with_color_black_or_grey(self):
        # Создать заказ самоката с ЧЕРНЫМ ИЛИ СЕРЫМ цветом
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        assert response.status_code == 201

    @allure.title('Создать заказ самоката черного и серого цвета')
    def test_create_order_with_color_black_and_grey(self):
        # Создать заказ самоката с ЧЕРНЫМ И СЕРЫМ цветом
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": ['BLACK', 'GREY']}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        assert response.status_code == 201

    @allure.title('Создать заказ самоката без цвета')
    def test_create_order_without_color(self):
        # Создать заказ самоката без указания цвета
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": ['']}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        assert response.status_code == 201

    @allure.title('Создать заказ и получить номер заказа')
    def test_create_order_return_code_track_order(self):
        # Создать заказ самоката с ЧЕРНЫМ ИЛИ СЕРЫМ цветом
        payload_order = {"firstName": generate_first_name(), "lastName": generate_password(),
                         "address": generate_address(),
                         "metroStation": generate_metro_station(), "phone": generate_phone(),
                         "rentTime": generate_rent_time(), "deliveryDate": generate_delivery_date(),
                         "comment": generate_comment(),
                         "color": generate_color()}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER_URL}', json=payload_order)

        assert 'track' in response.json()