from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql, QtGui, QtWidgets, QtCore

class Ui_NewService(QtWidgets.QWidget):
    def __init__(self, model, flag, data, currIndex):
        self.model = model
        self.flag = flag
        self.data = data
        self.currIndex = currIndex
        super().__init__()
        self.setupUi(self)
    def setupUi(self, NewService):
        NewService.setObjectName("NewService")
        NewService.setFixedSize(601, 288)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2 = QtWidgets.QLabel(NewService)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(NewService)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 191, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_8 = QtWidgets.QLabel(NewService)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 151, 31))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.textEdit_2 = QtWidgets.QTextEdit(NewService)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 50, 321, 41))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(NewService)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 100, 321, 41))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")

        self.pushButton_7 = QtWidgets.QPushButton(NewService)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 210, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        if self.flag == 0:
            self.pushButton_7.clicked.connect(self.newRecord)
        if self.flag == 1:
            self.pushButton_7.clicked.connect(self.editRecord)

        self.textEdit_7 = QtWidgets.QTextEdit(NewService)
        self.textEdit_7.setGeometry(QtCore.QRect(240, 150, 251, 41))
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")

        self.textEdit_8 = QtWidgets.QTextEdit(NewService)
        self.textEdit_8.setGeometry(QtCore.QRect(500, 150, 61, 41))
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")

        self.retranslateUi(NewService)
        QtCore.QMetaObject.connectSlotsByName(NewService)

        self.query = QtSql.QSqlQuery('serv.db')

        if self.flag == 1:
            self.textEdit_2.setText(self.data[0])
            self.textEdit_3.setText(self.data[1])
            self.textEdit_7.setText(self.data[2])
            self.textEdit_8.setText(self.data[3])

    def retranslateUi(self, NewService):
        _translate = QtCore.QCoreApplication.translate
        NewService.setWindowTitle(_translate("NewService", "Новая услуга"))
        self.label_2.setText(_translate("NewService", "Название"))
        self.label_3.setText(_translate("NewService", "Цена"))
        self.label_8.setText(_translate("NewService", "Фурнитура"))
        self.pushButton_7.setText(_translate("NewService", "Записать"))

    def newRecord(self):
        self.query.exec_(f"INSERT INTO service VALUES ('{self.textEdit_2.toPlainText()}', '{self.textEdit_3.toPlainText()}', '{self.textEdit_7.toPlainText()}', '{self.textEdit_8.toPlainText()}')")
        self.model.select()
        self.query.exec_("select rowid, * FROM service")
        self.model.select()

    def editRecord(self):
        self.query.exec_(f"UPDATE service SET Название = '{self.textEdit_2.toPlainText()}' WHERE rowid = {self.currIndex.row() + 1}")
        self.query.exec_(f"UPDATE service SET Цена = '{self.textEdit_3.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE service SET Фурнитура = '{self.textEdit_7.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE service SET Колво_фурнитуры = '{self.textEdit_8.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.model.select()