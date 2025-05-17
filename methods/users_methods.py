import allure
from src.urls import Urls
from methods.base_methods import BaseMethods


class UsersMethods:

    @allure.step('Создание пользователя')
    def user_create(self, payload):
        url = Urls.user_create
        return BaseMethods.post_request(url, payload)

    @allure.step('Авторизация пользователя')
    def user_login(self, email, password):
        payload = {
            "email": email,
            "password": password}
        url = Urls.user_login
        return BaseMethods.post_request(url, payload)

    @allure.step('Удаление пользователя')
    def user_delete(self, access_token):
        headers = {'Authorization': access_token}
        url = Urls.user_delete
        return BaseMethods.delete_request(url, headers)

    @allure.step('Создание пользователя и получение его email и пароля')
    def user_email_pass_name_registration(self, payload):
        email_pass_name = {}
        response = self.user_create(payload)
        if response.status_code == 200:
            email_pass_name['email'] = payload['email']
            email_pass_name['password'] = payload['password']
            email_pass_name['name'] = payload['name']
        return email_pass_name

    @allure.step('Изменение данных пользователя')
    def user_update(self, access_token, new_data):
        headers = {'Authorization': access_token}
        url = Urls.user_update_info
        return BaseMethods.patch_request(url, headers, new_data)
