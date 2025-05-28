import allure
from src.data import OrderData
from src.data import Message


class TestOrderReceive:

    @allure.title('Проверка получения списка заказов авторизованного пользователя')
    def test_order_receive_with_authorization(self, user_data_with_delete_user, user_methods, orders_methods):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass_name['email']
        password = email_pass_name['password']
        access_token = user_methods.user_login(email, password).json()['accessToken']
        ingredients = OrderData.order_data_with_ingredients
        orders_methods.order_create_with_authorization(ingredients, access_token)
        response = orders_methods.order_receive_with_authorization(access_token)

        assert response.status_code == 200
        assert response.json()['success'] == Message.order_status_success

    @allure.title('Проверка ошибки получения списка заказов неавторизованного пользователя')
    def test_order_receive_without_authorization(self, user_data_with_delete_user, user_methods, orders_methods):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass_name['email']
        password = email_pass_name['password']
        access_token = user_methods.user_login(email, password).json()['accessToken']
        ingredients = OrderData.order_data_with_ingredients
        orders_methods.order_create_with_authorization(ingredients, access_token)
        response = orders_methods.order_receive_without_authorization()

        assert response.status_code == 401
        assert response.json()['message'] == Message.user_unauthorized
