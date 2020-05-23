"""
Программа позволяет зарегистрироваться в игровом портале и сыграть на выбор в игру
Во время регистрации происходит валидация логина и пароля с помощью регулярных выражений

"""
from users import User
from validation import Validate
from random import randint

print("Добро пожаловать в игровой портал с двумя играми: змейка и сапер!\n")


def program():
    print(
        "Логин должен начинаться с буквы и состоять не менее чем из 4 символов и не более чем из 20 символов;\n"
        "при создании логина можно использовать латинские буквы, цифры, символы тире (-), подчеркивания (_) и точки (.)\n")

    user_login = input("Введите логин: " '\n')
    while Validate.validate_login(user_login) is None:
        print("Ошибка! Попробуйте еще раз")
        user_login = input("Введите логин: ")

    print("Пароль должен содержать не менее 8 символов\n")
    user_password = input("Введите пароль: ")
    while Validate.validate_password(user_password) is None:
        print("Ошибка! Попробуйте еще раз")
        user_password = input("Введите пароль: ")

    user = User(user_login, user_password, randint(1, 999999))

    print("login: " + user.login)
    print("password: " + user.password)
    print("id: " + str(user.uniq_id))

    user_data = ("login: " + str(user.login) + "\npassword: " + str(user.password) + "\nuniq_id: " + str(user.uniq_id))

    user_file = str(user.login) + "_" + str(randint(1, 999999)) + ".txt"
    s = open(user_file, 'w')
    s.write(str(user_data) + '\n')
    s.close()
    print("Файл '" + user_file + "' успешно сохранен")


User.greet(program)

play = input("В какую игру вы хотите сыграть?\n1 - Змейка\n2 - Сапер")
if play == "1":
    import snake
elif play == "2":
    import sapper
