from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from PyQt5.QtCore import Qt
class Ui_searchServise(QtWidgets.QWidget):
    def __init__(self, model, tableView):
        self.model = model
        self.tableView = tableView
        super().__init__()
        self.setupUi(self)
    def setupUi(self, searchServise):
        searchServise.setObjectName("searchServise")
        searchServise.setFixedSize(601, 265)
        self.label = QtWidgets.QLabel(searchServise)
        self.label.setGeometry(QtCore.QRect(40, 110, 101, 21))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit_2 = QtWidgets.QTextEdit(searchServise)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 100, 321, 41))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_7 = QtWidgets.QPushButton(searchServise)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 190, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.search)

        self.query = QtSql.QSqlQuery('serv.db')
        self.retranslateUi(searchServise)
        QtCore.QMetaObject.connectSlotsByName(searchServise)
    def search(self):
        from PyQt5.QtWidgets import QAbstractItemView
        from PyQt5.QtWidgets import QMessageBox
        text = self.textEdit_2.toPlainText()
        if text == "": # проверка на то что пользователь ничего не ввел
            QMessageBox.about(self, "Ошибка", "Введите услугу")
        indexes = self.tableView.model().match(self.tableView.model().index(0, 0), Qt.EditRole, text, -1, Qt.MatchFlags(Qt.MatchContains | Qt.MatchWrap))# список со совпадающими элементами
        if (len(indexes) > 0):# если список больше нуля выдавать результат иначе сообщить о том что такой услуги не найдено
            self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)
            for i in indexes:
                self.tableView.selectRow(i.row()) # выделить найденную строку
        else: QMessageBox.about(self, "Ошибка", "Услуга не найдена")

    def retranslateUi(self, searchServise):
        _translate = QtCore.QCoreApplication.translate
        searchServise.setWindowTitle(_translate("search", "Поиск"))
        self.label.setText(_translate("search", "Услуга"))
        self.pushButton_7.setText(_translate("search", "Поиск"))
