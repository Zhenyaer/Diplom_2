class Urls:
    user_create = 'https://stellarburgers.nomoreparties.site/api/auth/register' #POST, создание пользователя
    user_login = ' https://stellarburgers.nomoreparties.site/api/auth/login'  #POST, авторизация пользователя
    user_update_info = ' https://stellarburgers.nomoreparties.site/api/auth/user'  #PATCH, изменение данных пользователя
    user_delete = 'https://stellarburgers.nomoreparties.site/api/auth/user'  #DELETE, удаление пользователя
    order_create = 'https://stellarburgers.nomoreparties.site/api/orders'  #POST, создание заказа
    order_receive = 'https://stellarburgers.nomoreparties.site/api/orders' #GET, получение заказов пользователя
