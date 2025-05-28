import pytest
import allure
from src.data import Message


class TestUserCreate:

    @allure.title('Проверка создания пользователя')
    def test_user_create(self, user_data_with_delete_user, user_methods):
        response = user_methods.user_create(user_data_with_delete_user)

        assert response.status_code == 200
        assert (response.json()['user']['email'] == user_data_with_delete_user['email'] and
                response.json()['user']['name'] == user_data_with_delete_user['name'])

    @allure.title('Проверка невозможности регистрации существующего пользователя')
    def test_user_create_already_registered(self, user_data_with_delete_user, user_methods):
        user_methods.user_create(user_data_with_delete_user)
        response = user_methods.user_create(user_data_with_delete_user)

        assert response.status_code == 403
        assert response.json()['message'] == Message.user_exists

    @allure.title('Проверка невозможности создания пользователя при отсутствии одного из обязательных полей')
    @pytest.mark.parametrize('empty_field', ['email', 'password', 'name'])
    def test_user_none_create_without_required_field(self, user_data, empty_field, user_methods):
        user_data[empty_field] = ''
        response = user_methods.user_create(user_data)

        assert response.status_code == 403
        assert response.json()['message'] == Message.user_none_create_without_required_fields
