import allure
from src.urls import Urls
from methods.base_methods import BaseMethods


class OrdersMethods:

    @allure.step('Создание заказа с авторизацией')
    def order_create_with_authorization(self, ingredients, access_token):
        headers = {'Authorization': access_token}
        url = Urls.order_create
        return BaseMethods.post_request_with_headers(url, ingredients, headers)

    @allure.step('Создание заказа без авторизации')
    def order_create_without_authorization(self, ingredients):
        url = Urls.order_create
        return BaseMethods.post_request(url, ingredients)

    @allure.step('Получение списка заказов авторизованного пользователя')
    def order_receive_with_authorization(self, access_token):
        headers = {'Authorization': access_token}
        url = Urls.order_receive
        return BaseMethods.get_request_with_headers(url, headers)

    @allure.step('Получение списка заказов неавторизованного пользователя')
    def order_receive_without_authorization(self):
        url = Urls.order_receive
        return BaseMethods.get_request(url)
