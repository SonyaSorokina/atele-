from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui, QtWidgets
from clientsewing import*
from lib import listService, sendMessage

class Ui_EditSewing(QtWidgets.QWidget):
    def __init__(self, model, data, currIndex, * args):
        self.l = listService()

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('sewdb.db')
        db.open()

        self.model = model
        self.data = data
        self.currIndex = currIndex
        super().__init__()
        self.setupUi(self)
    def setupUi(self, EditSewing):
        EditSewing.setObjectName("EditSewing")
        EditSewing.setFixedSize(601, 639)
        self.label = QtWidgets.QLabel(EditSewing)
        self.label.setGeometry(QtCore.QRect(40, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(EditSewing)
        self.textEdit.setGeometry(QtCore.QRect(240, 50, 321, 41))
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(EditSewing)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 191, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(EditSewing)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 191, 21))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(EditSewing)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 71, 21))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.comboBox = QtWidgets.QComboBox(EditSewing)
        self.comboBox.setGeometry(QtCore.QRect(240, 200, 321, 41))
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        for i in self.l:
            self.comboBox.addItem(i.get('Услуга'))

        self.label_6 = QtWidgets.QLabel(EditSewing)
        self.label_6.setGeometry(QtCore.QRect(40, 260, 151, 21))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(EditSewing)
        self.label_7.setGeometry(QtCore.QRect(40, 310, 151, 21))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(EditSewing)
        self.label_8.setGeometry(QtCore.QRect(40, 360, 151, 31))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(EditSewing)
        self.label_9.setGeometry(QtCore.QRect(40, 410, 151, 21))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(EditSewing)
        self.label_10.setGeometry(QtCore.QRect(40, 460, 151, 21))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.textEdit_2 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 100, 321, 41))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 150, 321, 41))
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_4.setGeometry(QtCore.QRect(240, 300, 321, 41))
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_5.setGeometry(QtCore.QRect(240, 250, 321, 41))
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")

        self.textEdit_6 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_6.setGeometry(QtCore.QRect(240, 450, 321, 41))
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")

        self.dateEdit = QtWidgets.QDateEdit(EditSewing)
        self.dateEdit.setGeometry(QtCore.QRect(240, 400, 321, 41))
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")

        self.pushButton_7 = QtWidgets.QPushButton(EditSewing)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 570, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        self.textEdit_7 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_7.setGeometry(QtCore.QRect(240, 350, 251, 41))
        self.textEdit_7.setFont(font)
        self.textEdit_7.setObjectName("textEdit_7")

        self.pushButton_7.clicked.connect(self.editRecord)

        self.textEdit_8 = QtWidgets.QTextEdit(EditSewing)
        self.textEdit_8.setGeometry(QtCore.QRect(500, 350, 61, 41))
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")

        self.label_11 = QtWidgets.QLabel(EditSewing)
        self.label_11.setGeometry(QtCore.QRect(40, 510, 151, 21))
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.comboBox_2 = QtWidgets.QComboBox(EditSewing)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 500, 321, 41))
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem('Принят')
        self.comboBox_2.addItem('Готов')

        self.retranslateUi(EditSewing)
        QtCore.QMetaObject.connectSlotsByName(EditSewing)

        self.textEdit.setText(self.data[0])
        self.textEdit_2.setText(self.data[1])
        self.textEdit_3.setText(self.data[2])
        self.comboBox.setCurrentText(self.data[3])
        self.textEdit_5.setText(self.data[4])
        self.textEdit_4.setText(self.data[5])
        self.textEdit_7.setText(self.data[6])
        self.textEdit_8.setText(self.data[7])
        self.dateEdit.setDate(QtCore.QDate(int(self.data[8][:4:]),int(self.data[8][5:7:]),int(self.data[8][8:])))
        self.textEdit_6.setText(self.data[10])

    def retranslateUi(self, EditSewing):
        _translate = QtCore.QCoreApplication.translate
        EditSewing.setWindowTitle(_translate("EditSewing", "Редактировать запись"))
        self.label.setText(_translate("EditSewing", "ФИО"))
        self.label_2.setText(_translate("EditSewing", "Мобильный телефон"))
        self.label_3.setText(_translate("EditSewing", "Электронна почта"))
        self.label_5.setText(_translate("EditSewing", "Услуга"))
        self.label_6.setText(_translate("EditSewing", "Снятые мерки"))
        self.label_7.setText(_translate("EditSewing", "Материал"))
        self.label_8.setText(_translate("EditSewing", "Фурнитура"))
        self.label_9.setText(_translate("EditSewing", "Крайний срок"))
        self.label_10.setText(_translate("EditSewing", "Цена"))
        self.pushButton_7.setText(_translate("EditSewing", "Записать"))
        self.label_11.setText(_translate("EditSewing", "Статус"))

    def editRecord(self):
        self.query = QtSql.QSqlQuery('sewdb.db')
        self.query.exec_(f"UPDATE sewing SET ФИО = '{self.textEdit.toPlainText()}' WHERE rowid = {self.currIndex.row()+1}")
        self.query.exec_(f"UPDATE sewing SET Мобильный_телефон = '{self.textEdit_2.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Электронная_почта = '{self.textEdit_3.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Услуга = '{self.comboBox.currentText()}' WHERE rowid = {self.currIndex.row() + 1}")
        self.query.exec_(f"UPDATE sewing SET Снятые_мерки = '{self.textEdit_5.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Материал = '{self.textEdit_4.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Фурнитура = '{self.textEdit_7.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Колво_фурнитуры = '{self.textEdit_8.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Крайний_срок = '{self.dateEdit.date().toPyDate()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Статус = '{self.comboBox_2.currentText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.query.exec_(f"UPDATE sewing SET Цена = '{self.textEdit_6.toPlainText()}' WHERE rowid = {self.currIndex.row()+ 1}")
        self.model.select()
        self.query.exec_("select rowid, * FROM sewing")
        self.model.select()
        if self.comboBox_2.currentText()=='Готов':
            sendMessage(self.textEdit_2.toPlainText())