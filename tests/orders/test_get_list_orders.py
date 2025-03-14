import allure
import requests

from data import LIMIT_ORDERS, MAIN_URL, GET_LIST_ORDERS_URL


class TestListOrders:

    @allure.title('Получить заказы и проверить тело ответа возвращает список заказов')
    def test_get_orders_return_list_orders(self):
        # Получить список заказов
        params = {"limit": LIMIT_ORDERS}
        response = requests.get(f'{MAIN_URL}{GET_LIST_ORDERS_URL}', params=params)

        assert len(response.json()['orders']) == LIMIT_ORDERS