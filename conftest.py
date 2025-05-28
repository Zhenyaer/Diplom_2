import pytest
from src.data import create_user_data
from methods.users_methods import UsersMethods
from src.data import ChangeInfo
from methods.orders_methods import OrdersMethods


@pytest.fixture()
def user_data_with_delete_user():
    payload = create_user_data()
    yield payload
    email = payload['email']
    password = payload['password']
    response = UsersMethods()
    if response.user_login(email, password).status_code == 200:
        access_token = response.user_login(email, password).json()['accessToken']
    else:
        email = f'{ChangeInfo.prefix}{payload['email']}'
        access_token = response.user_login(email, password).json()['accessToken']
    response.user_delete(access_token)


@pytest.fixture()
def user_data():
    payload = create_user_data()
    yield payload


@pytest.fixture()
def user_methods():
    yield UsersMethods()


@pytest.fixture()
def orders_methods():
    yield OrdersMethods()
