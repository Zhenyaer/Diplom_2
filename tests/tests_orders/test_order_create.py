import allure
from src.data import OrderData
from src.data import Message


class TestOrderCreate:

    @allure.title('Проверка создания заказа с ингридиентами авторизованным пользователем')
    def test_order_create_with_authorization(self, user_data_with_delete_user, user_methods, orders_methods):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass_name['email']
        password = email_pass_name['password']
        access_token = user_methods.user_login(email, password).json()['accessToken']
        ingredients = OrderData.order_data_with_ingredients
        response = orders_methods.order_create_with_authorization(ingredients, access_token)

        assert response.status_code == 200
        assert response.json()['success'] == Message.order_status_success

    @allure.title('Проверка создания заказа с ингридиентами неавторизованным пользователем')
    def test_order_create_without_authorization(self, orders_methods):
        ingredients = OrderData.order_data_with_ingredients
        response = orders_methods.order_create_without_authorization(ingredients)

        assert response.status_code == 200
        assert response.json()['success'] == Message.order_status_success

    @allure.title('Проверка ошибки при создании заказа без ингридиентов')
    def test_order_create_without_ingredients(self, user_data_with_delete_user, user_methods, orders_methods):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass_name['email']
        password = email_pass_name['password']
        access_token = user_methods.user_login(email, password).json()['accessToken']
        ingredients = OrderData.order_data_without_ingredients
        response = orders_methods.order_create_with_authorization(ingredients, access_token)

        assert response.status_code == 400
        assert response.json()['message'] == Message.order_error_empty_ingredients

    @allure.title('Проверка ошибки при создании заказа c неверным хэшем ингридиентов')
    def test_order_create_with_false_ingredients(self, user_data_with_delete_user, user_methods, orders_methods):
        email_pass_name = user_methods.user_email_pass_name_registration(user_data_with_delete_user)
        email = email_pass_name['email']
        password = email_pass_name['password']
        access_token = user_methods.user_login(email, password).json()['accessToken']
        ingredients = OrderData.order_data_with_false_ingredients
        response = orders_methods.order_create_with_authorization(ingredients, access_token)

        assert response.status_code == 500
