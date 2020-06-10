from PyQt5.Qt import *
from signup import Dialog
import json



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 290)
        self.login_label = QLabel(Dialog)
        self.login_label.setGeometry(QRect(150, 100, 80, 20))
        font = QFont()
        font.setPointSize(10)
        self.login_label.setFont(font)
        self.login_label.setAlignment(Qt.AlignCenter)
        self.login_label.setObjectName("u_name_label")
        self.pass_label = QLabel(Dialog)
        self.pass_label.setGeometry(QRect(150, 150, 71, 21))
        font = QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")

        self.uname_lineEdit = QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")

        self.pass_lineEdit = QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QRect(230, 150, 113, 20))
        self.pass_lineEdit.setObjectName("pass_lineEdit")

        self.login_btn = QPushButton(Dialog)
        self.login_btn.setGeometry(QRect(230, 200, 60, 25))
        self.login_btn.setObjectName("login_btn")

        self.signup_btn = QPushButton(Dialog)
        self.signup_btn.setGeometry(QRect(290, 200, 100, 25))
        self.signup_btn.setObjectName("signup_btn")

        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(190, 10, 210, 60))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.Ui_translate(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def Ui_translate(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация в игровой портал"))
        self.login_label.setText(_translate("Dialog", "Логин "))
        self.pass_label.setText(_translate("Dialog", "Пароль"))
        self.login_btn.setText(_translate("Dialog", "Вход"))
        self.signup_btn.setText(_translate("Dialog", "Регистрация"))
        self.label.setText(_translate("Dialog", "Авторизация"))


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.login_btn.clicked.connect(self.loginCheck)
        self.signup_btn.clicked.connect(self.signUpCheck)

    def signUpShow(self):
        self.signUpWindow = Dialog(self)
        self.signUpWindow.show()

    def loginCheck(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()

        if (not username) or (not password):
            msg = QMessageBox.information(self, 'Внимание!', 'Вы не заполнили все поля.')
            return

        else:
            msg = QMessageBox.information(self, 'Внимание!', 'Вход в данный момент невозможен, попробуйте зарегистрироваться.')
        # filename = "all_users.json"
        # with open(filename) as file:
        #     data = json.load(file)
        #     print(data)

    def signUpCheck(self):
        self.signUpShow()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainDialog()
    w.show()
    sys.exit(app.exec_())
