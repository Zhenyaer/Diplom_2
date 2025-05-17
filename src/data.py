import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_user_data():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    username = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": username
    }
    return payload


class Message:
    user_exists = 'User already exists'
    user_none_create_without_required_fields = 'Email, password and name are required fields'
    user_none_login_with_incorrect_data = 'email or password are incorrect'
    user_unauthorized = 'You should be authorised'
    order_status_success = True
    order_error_empty_ingredients = 'Ingredient ids must be provided'


class ChangeInfo:
    prefix = 'new'


class OrderData:
    order_data_with_ingredients = {}
    order_data_without_ingredients = {}
    order_data_with_false_ingredients = {}
    ingredients = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa70']
    false_ingredients = ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa705678']
    order_data_with_ingredients['ingredients'] = ingredients
    order_data_without_ingredients['ingredients'] = []
    order_data_with_false_ingredients['ingredients'] = false_ingredients
