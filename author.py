from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_author(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, author):
        author.setObjectName("author")
        author.setFixedSize(405, 165)
        self.label = QtWidgets.QLabel(author)
        self.label.setGeometry(QtCore.QRect(50, 40, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(author)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 251, 41))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(author)
        QtCore.QMetaObject.connectSlotsByName(author)

    def retranslateUi(self, author):
        _translate = QtCore.QCoreApplication.translate
        author.setWindowTitle(_translate("author", "Об авторе"))
        self.label.setText(_translate("author", "Автор программы: Сорокина Софья"))
        self.label_2.setText(_translate("author", "студентка группы ПИН-222"))
