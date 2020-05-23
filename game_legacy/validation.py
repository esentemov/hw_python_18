from re import fullmatch


class Validate():
    """Валидация

    """

    regular_login = r"^[a-zA-Z0-9\._-]{4,20}$"
    """Регулярное выражение для проверки логина пользователя.
    Логин должен начинаться с буквы и состоять не менее чем из 4 символов и не более чем из 20 символов;
    при создании логина можно использовать латинские буквы, цифры, символы тире (-), подчеркивания (_) и точки (.)
    
    """

    regular_password = r"[A-Za-z0-9@#$%^&+=]{8,}$"
    """Регулярное выржание для проверки пароля пользователя.
    Пароль должен содержать не менее 8 символов.
    
    """

    @staticmethod
    def validate_login(user_login):
        return fullmatch(Validate.regular_login, user_login)

    @staticmethod
    def validate_password(user_password):
        return fullmatch(Validate.regular_password, user_password)
