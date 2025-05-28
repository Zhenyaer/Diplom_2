import pytest
import allure
from src.data import Message
from src.data import ChangeInfo


class TestUserChangeData:

    @allure.title('Проверка изменения данных авторизованного пользователя')
    @pytest.mark.parametrize('change_data', ['email', 'name'])
    def test_user_change_data_with_authorization(self, user_data_with_delete_user, user_methods, change_data):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass_name['email']
        password = email_pass_name['password']
        new_data = email_pass_name
        new_data[change_data] = f'{ChangeInfo.prefix}{new_data[change_data]}'
        access_token = user_methods.user_login(email, password).json()['accessToken']
        response = user_methods.user_update(access_token, new_data)

        assert response.status_code == 200
        assert (response.json()['user']['email'] == new_data['email'] and
                response.json()['user']['name'] == new_data['name'])

    @allure.title('Проверка возникновении ошибки при попытке изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize('change_data', ['email', 'name'])
    def test_user_change_data_without_authorization(self, user_data, user_methods, change_data):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data)
        new_data = email_pass_name
        new_data[change_data] = f'{ChangeInfo.prefix}{new_data[change_data]}'
        access_token = ''
        response = user_methods.user_update(access_token, new_data)

        assert response.status_code == 401
        assert response.json()['message'] == Message.user_unauthorized
