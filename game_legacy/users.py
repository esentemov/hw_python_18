import json

class User:
    """Класс пользователя

    """

    def __init__(self, login, password, uniq_id):
        """Инициализирует атрибуты:
        - логин
        - пароль
        - id

        """
        self.login = login
        self.password = password
        self.uniq_id = uniq_id

    # def greet(program):
    #
    #     """Спрашивает User,  зарегистрирован ли он в системе.
    #      Если нет, то предлагает зарегистрироваться.
    #      (login и пароль проверяются на регулярных выражениях, а атрибут uniq_id генерируется программно)
    #
    #      """
    #
    #     sign_in = input("Вы зарегистрированы на портале? ").strip().lower()
    #     if sign_in == "нет":
    #
    #         program()
    #
    #     else:
    #         print("Зарегистируйтесь еще раз")
    #         program()


