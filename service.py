from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from newservice import *
from searchServise import *
from PyQt5.QtWidgets import QStyledItemDelegate, QAbstractItemDelegate, QWidget, QAbstractItemView
from PyQt5 import QtSql, QtGui, QtWidgets, QtCore

class ReadOnlyDelegate(QStyledItemDelegate): #функция которая не разрешает редактировать tableView
    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        return None
class Ui_service(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, service):
        service.setObjectName("service")
        service.setFixedSize(1024, 640)
        self.tableView = QtWidgets.QTableView(service)
        self.tableView.setGeometry(QtCore.QRect(10, 120, 1000, 500))
        self.tableView.setObjectName("tableView")

        self.pushButton_4 = QtWidgets.QPushButton(service)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 30, 230, 50))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.newSearch)

        self.pushButton_6 = QtWidgets.QPushButton(service)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 30, 230, 50))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.newService)

        self.pushButton_7 = QtWidgets.QPushButton(service)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 30, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.deleteServise)

        self.retranslateUi(service)
        QtCore.QMetaObject.connectSlotsByName(service)

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE') #подключаем базу данных с услугами
        db.setDatabaseName('serv.db')
        db.open()

        query = QtSql.QSqlQuery('serv.db') #создание запроса

        query.exec_("create table service (Название varchar(50))")# задаем столбцы таблице service
        query.exec_("alter table service add Цена varchar(50)")
        query.exec_("alter table service add Фурнитура varchar(50)")
        query.exec_("alter table service add Колво_фурнитуры varchar(50)")

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('service')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.setWindowTitle("service")
        self.tableView.setItemDelegate(ReadOnlyDelegate())

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        query.exec_("select rowid, * FROM service")

        self.tableView.doubleClicked.connect(self.editService) # сигнал срабатывающий при двойном клике на tableView


    def newService(self): # функция создания новой услуги
        flag = 0
        data = []
        currIndex = 0
        self.type_window = Ui_NewService(self.model, flag, data, currIndex)
        self.type_window.show()

    def editService(self):# функция редактирования услуги
        flag = 1
        currIndex = self.tableView.currentIndex()
        data = []
        for column in range(self.model.columnCount()): # в список data мы собираем данные по колонкам в той строке которую выбрал пользователь
            item = self.tableView.model().index(currIndex.row(), column).data()
            if item is None:
                data.append("")
            else:
                data.append(item)
        print(data)
        self.type_window = Ui_NewService(self.model, flag, data, currIndex)
        self.type_window.show()
    def deleteServise(self):# функция удаления услуги
        query = QtSql.QSqlQuery('serv.db')
        indices = self.tableView.selectedIndexes()
        for index in sorted(indices):
            print(index.row())
            self.model.deleteRowFromTable(index.row())
            query.exec_(f"DELETE FROM serv WHERE rowid = {index.row()}")
        self.model.select()

    def newSearch(self):# функция открытия окна с поиском
        self.type_window = Ui_searchServise(self.model, self.tableView)
        self.type_window.show()


    def retranslateUi(self, service):
        _translate = QtCore.QCoreApplication.translate
        service.setWindowTitle(_translate("service", "Услуги"))
        self.pushButton_4.setText(_translate("service", "Поиск"))
        self.pushButton_6.setText(_translate("service", "Новая услуга"))
        self.pushButton_7.setText(_translate("service", "Удалить"))
