import allure
import requests
import logging
from data import LIMIT_ORDERS, MAIN_URL, GET_LIST_ORDERS_URL

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений
    handlers=[logging.StreamHandler()]  # Вывод в консоль
)


class TestListOrders:

    @allure.title('Получить заказы и проверить тело ответа возвращает список заказов')
    def test_get_orders_return_list_orders(self):
        # Получить список заказов
        params = {"limit": LIMIT_ORDERS}
        response = requests.get(f'{MAIN_URL}{GET_LIST_ORDERS_URL}', params=params)

        # Логирование запроса и ответа
        logging.info(f"Запрос на получение списка заказов: {params}")
        logging.info(f"Ответ сервера: {response.status_code}, {response.json()}")

        assert len(response.json()['orders']) == LIMIT_ORDERS