from helpers import generate_login, generate_password, generate_first_name, generate_limit_orders, \
    generate_courier_id

MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
CREATE_COURIER_URL = '/api/v1/courier'
DELETE_COURIER_URL = '/api/v1/courier/{id}'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
GET_LIST_ORDERS_URL = '/api/v1/orders'
ACCEPT_ORDER_URL = '/api/v1/orders/accept'
GET_ORDER_BY_ID_URL = '/api/v1/orders/track'
LOGIN = generate_login()
PASSWORD = generate_password()
FIRST_NAME = generate_first_name()
LIMIT_ORDERS = generate_limit_orders()
COURIER_ID = generate_courier_id()