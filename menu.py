from clientsewing import *
from service import *
from author import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.setFixedSize(1024, 640)
        font = QtGui.QFont()
        font.setPointSize(14)
        Menu.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Menu)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 371, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.openClient)

        self.pushButton_2 = QtWidgets.QPushButton(Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 290, 371, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.openService)

        self.pushButton_3 = QtWidgets.QPushButton(Menu)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 360, 371, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.autor)

        self.label = QtWidgets.QLabel(Menu)
        self.label.setGeometry(QtCore.QRect(620, 280, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)
    def openClient(self): #функция открывающая окно с записями клиентов
        self.type_window = Ui_ClientSewing()
        self.type_window.show()

    def openService(self): #функция открывающая окно с услугами
        self.type_window = Ui_service()
        self.type_window.show()

    def autor(self): #функция открывающая окно с автором
        self.type_window = Ui_author()
        self.type_window.show()

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Меню"))
        self.pushButton.setText(_translate("Menu", "Заказы"))
        self.pushButton_2.setText(_translate("Menu", "Услуги"))
        self.pushButton_3.setText(_translate("Menu", "Об авторе"))
        self.label.setText(_translate("Menu", "Ателье +"))

    def closeEvent(self, event):
        self.type_window.close()
        self.close()
        event.accept()

if __name__ == "__main__":
    global db
    import sys
    app = QtWidgets.QApplication(sys.argv)

    type_window = Ui_Menu()
    type_window.show()
    sys.exit(app.exec_())
