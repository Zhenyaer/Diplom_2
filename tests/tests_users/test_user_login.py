import pytest
import allure
from src.data import Message


class TestUserLogin:

    @allure.title('Проверка авторизации существующего пользователя')
    def test_user_login(self, user_data_with_delete_user, user_methods):
        email_pass = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass['email']
        password = email_pass['password']
        response = user_methods.user_login(email, password)

        assert response.status_code == 200
        assert (response.json()['user']['email'] == user_data_with_delete_user['email'] and
                response.json()['user']['name'] == user_data_with_delete_user['name'])

    @allure.title('Проверка ошибки авторизации при неверном логине/пароле')
    @pytest.mark.parametrize('false_field', ['email', 'password'])
    def test_user_none_login_with_incorrect_data(self, user_data, user_methods, false_field):
        email_pass = user_methods.user_email_pass_name_registration(user_data)
        email_pass[false_field] = f'579{false_field}'
        email = email_pass['email']
        password = email_pass['password']
        response = user_methods.user_login(email, password)

        assert response.status_code == 401
        assert response.json()['message'] == Message.user_none_login_with_incorrect_data
