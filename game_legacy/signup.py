from PyQt5.Qt import *
from validation import Validate
from random import randint
from users import User
import json
from ui_game import Dialog2


class UI_signUp(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 375)
        self.label_1 = QLabel(Dialog)
        self.label_1.setGeometry(QRect(160, 130, 81, 31))
        font = QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(160, 180, 81, 31))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.name_lineEdit = QLineEdit(Dialog)
        self.name_lineEdit.setGeometry(QRect(250, 130, 141, 20))
        self.name_lineEdit.setObjectName("name_lineEdit")

        self.password_lineEdit = QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QRect(250, 180, 141, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(210, 240, 175, 43))
        self.signup_btn.setObjectName("signup_btn")

        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(150, 10, 321, 81))
        font = QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.UI_translate(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def UI_translate(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Регистрация в игровом портале"))
        self.label_3.setText(_translate("Dialog", "Создайте аккаунт"))
        self.label_1.setText(_translate("Dialog", "Логин"))
        self.label_2.setText(_translate("Dialog", "Пароль"))
        self.signup_btn.setText(_translate("Dialog", "Зарегистрироваться"))


class Dialog(QDialog, UI_signUp):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.signup_btn.clicked.connect(self.insertData)

    def insertData(self):
        username = self.name_lineEdit.text()

        password = self.password_lineEdit.text()

        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return

        if Validate.validate_login(username) is None and Validate.validate_password(password) is None:
            msg = QMessageBox.information(self, 'Внимание!', 'И логин и пароль введены неправильно')
            return

        if Validate.validate_login(username) is None:
            msg = QMessageBox.information(self, 'Внимание!', 'Такой логин задать нельзя')
            return

        if Validate.validate_password(password) is None:
            msg = QMessageBox.information(self, 'Внимание!', 'Такой пароль задать нельзя')
            return

        if Validate.validate_login(username) and Validate.validate_password(password):
            user = User(username, password, randint(1, 999999))

            spi = {'username': user.login, 'password': user.password, 'id': user.uniq_id}
            with open("all_users.json", 'a+') as file:
                json.dump(spi, file)

            msg = QMessageBox.information(self, 'Успех', str(spi))
            return


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    w = Dialog()
    w.show()

    sys.exit(app.exec_())
