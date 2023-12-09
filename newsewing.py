from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from lib import listService
class Ui_NewSewing(QtWidgets.QWidget):
    def __init__(self, model):
        self.l = listService()

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sewdb.db')
        db.open()

        self.model = model
        super().__init__()
        self.setupUi(self)

    def setupUi(self, NewSewing):
        NewSewing.setObjectName("NewSewing")
        NewSewing.setFixedSize(600, 620)
        self.label = QtWidgets.QLabel(NewSewing)
        self.label.setGeometry(QtCore.QRect(40, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(NewSewing)
        self.textEdit.setGeometry(QtCore.QRect(240, 50, 321, 41))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(NewSewing)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 191, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(NewSewing)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 191, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(NewSewing)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 71, 21))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox = QtWidgets.QComboBox(NewSewing)
        self.comboBox.setGeometry(QtCore.QRect(240, 200, 321, 41))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        for i in self.l:
            self.comboBox.addItem(i.get('Услуга'))

        self.comboBox.currentIndexChanged.connect(self.enterData)

        self.label_6 = QtWidgets.QLabel(NewSewing)
        self.label_6.setGeometry(QtCore.QRect(40, 260, 151, 21))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(NewSewing)
        self.label_7.setGeometry(QtCore.QRect(40, 310, 151, 21))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(NewSewing)
        self.label_8.setGeometry(QtCore.QRect(40, 350, 151, 31))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(NewSewing)
        self.label_9.setGeometry(QtCore.QRect(40, 410, 151, 21))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(NewSewing)
        self.label_10.setGeometry(QtCore.QRect(40, 460, 151, 21))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.textEdit_2 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 100, 321, 41))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 150, 321, 41))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_4.setGeometry(QtCore.QRect(240, 300, 321, 41))
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_5.setGeometry(QtCore.QRect(240, 250, 321, 41))
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")

        self.textEdit_7 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_7.setGeometry(QtCore.QRect(240, 350, 251, 41))
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")

        self.textEdit_8 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_8.setGeometry(QtCore.QRect(500, 350, 61, 41))
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")

        self.textEdit_6 = QtWidgets.QTextEdit(NewSewing)
        self.textEdit_6.setGeometry(QtCore.QRect(240, 450, 321, 41))
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")

        self.dateEdit = QtWidgets.QDateEdit(NewSewing)
        self.dateEdit.setGeometry(QtCore.QRect(240, 400, 321, 41))
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")

        self.pushButton_7 = QtWidgets.QPushButton(NewSewing)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 520, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.newRecord)

        self.retranslateUi(NewSewing)
        QtCore.QMetaObject.connectSlotsByName(NewSewing)
        self.query = QtSql.QSqlQuery('sewdb.db')

    def retranslateUi(self, NewSewing):
        _translate = QtCore.QCoreApplication.translate
        NewSewing.setWindowTitle(_translate("NewSewing", "Новый пошив"))
        self.label.setText(_translate("NewSewing", "ФИО"))
        self.label_2.setText(_translate("NewSewing", "Мобильный телефон"))
        self.label_3.setText(_translate("NewSewing", "Электронная почта"))
        self.label_5.setText(_translate("NewSewing", "Услуга"))
        self.label_6.setText(_translate("NewSewing", "Снятые мерки"))
        self.label_7.setText(_translate("NewSewing", "Материал"))
        self.label_8.setText(_translate("NewSewing", "Фурнитура"))
        self.label_9.setText(_translate("NewSewing", "Крайний срок"))
        self.label_10.setText(_translate("NewSewing", "Цена"))
        self.pushButton_7.setText(_translate("NewSewing", "Записать"))

    def newRecord(self):
        self.query.exec_(f"INSERT INTO sewing VALUES ('{self.textEdit.toPlainText()}', '{self.textEdit_2.toPlainText()}', '{self.textEdit_3.toPlainText()}', '{self.comboBox.currentText()}', '{self.textEdit_5.toPlainText()}', '{self.textEdit_4.toPlainText()}', '{self.textEdit_7.toPlainText()}', '{self.textEdit_8.toPlainText()}', '{self.dateEdit.date().toPyDate()}', '{'Принят'}', '{self.textEdit_6.toPlainText()}')")
        self.model.select()
        self.query.exec_("select rowid, * FROM sewing")
        self.model.select()

    def enterData(self):
        i = self.l[self.comboBox.currentIndex()]
        self.textEdit_7.setText(i.get('Фурнитура'))
        self.textEdit_8.setText(i.get('Колво Фурнитуры'))
        self.textEdit_6.setText(i.get('Цена'))

