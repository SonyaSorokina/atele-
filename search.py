from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from PyQt5.QtCore import Qt
class Ui_search(QtWidgets.QWidget):
    def __init__(self, model, tableView):
        self.model = model
        self.tableView = tableView
        super().__init__()
        self.setupUi(self)
    def setupUi(self, search):
        search.setObjectName("search")
        search.setFixedSize(601, 265)
        self.label = QtWidgets.QLabel(search)
        self.label.setGeometry(QtCore.QRect(40, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.textEdit_2 = QtWidgets.QTextEdit(search)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 100, 321, 41))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_7 = QtWidgets.QPushButton(search)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 190, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.search)

        self.query = QtSql.QSqlQuery('sewdb.db')
        self.retranslateUi(search)
        QtCore.QMetaObject.connectSlotsByName(search)
    def search(self):
        from PyQt5.QtWidgets import QAbstractItemView
        from PyQt5.QtWidgets import QMessageBox
        text = self.textEdit_2.toPlainText()
        if text == "":
            QMessageBox.about(self, "Ошибка", "Введите ФИО")
        indexes = self.tableView.model().match(self.tableView.model().index(0, 0), Qt.EditRole, text, -1, Qt.MatchFlags(Qt.MatchContains | Qt.MatchWrap))
        if (len(indexes) > 0):
            self.tableView.setSelectionMode(QAbstractItemView.MultiSelection)

            for i in indexes:
                try:
                    self.tableView.selectRow(i.row())
                except Exception as e:
                    print(e)
        else: QMessageBox.about(self, "Ошибка", "Клиент не найден")

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "Поиск"))
        self.label.setText(_translate("search", "ФИО"))
        self.pushButton_7.setText(_translate("search", "Поиск"))
