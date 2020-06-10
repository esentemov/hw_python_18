from PyQt5.Qt import *


class UI_game(object):
    def go_game(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 375)

        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(150, 10, 321, 81))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label_3")

        self.snake_btn = QPushButton(Dialog)
        self.snake_btn.setGeometry(QRect(300, 200, 100, 40))
        self.snake_btn.setObjectName("snake_btn")

        self.sapper_btn = QPushButton(Dialog)
        self.sapper_btn.setGeometry(QRect(200, 200, 100, 40))
        self.sapper_btn.setObjectName("sapper_btn")

        self.UI_translate(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def UI_translate(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Игровой портал"))
        self.snake_btn.setText(_translate("Dialog", "Змейка"))
        self.sapper_btn.setText(_translate("Dialog", "Сапер"))
        self.label.setText(_translate("Dialog", "Во что хотите сыграть?"))


    @staticmethod
    def snakegame():
        import snake

    @staticmethod
    def sappergame():
        import sapper


class Dialog2(QDialog, UI_game):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.go_game(self)
        self.parent = parent

        self.snake_btn.clicked.connect(self.snakegame)
        self.sapper_btn.clicked.connect(self.sappergame)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = Dialog2()
    w.show()
    sys.exit(app.exec_())
