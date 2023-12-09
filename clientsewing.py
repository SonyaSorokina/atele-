from PyQt5 import QtSql, QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QStyledItemDelegate, QAbstractItemDelegate, QWidget, QAbstractItemView
from PyQt5.QtCore import Qt
from newsewing import *
from search import *
from lib import Label, split_to_fit
from PyQt5.QtWidgets import QMessageBox
from editnewsewing import*

class ReadOnlyDelegate(QStyledItemDelegate): # функция которая не разрешает редактировать tableView
    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QtCore.QModelIndex) -> QWidget:
        return None
class Ui_ClientSewing(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, ClientSewing):
        ClientSewing.setObjectName("ClientSewing")
        ClientSewing.setFixedSize(1024, 640)

        self.tableView = QtWidgets.QTableView(ClientSewing)
        self.tableView.setGeometry(QtCore.QRect(10, 120, 1000, 500))
        self.tableView.setObjectName("tableView")

        self.pushButton_4 = QtWidgets.QPushButton(ClientSewing)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 30, 230, 50))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.newSearch)

        self.pushButton_5 = QtWidgets.QPushButton(ClientSewing)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 30, 230, 50))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.makeLabel)

        self.pushButton_6 = QtWidgets.QPushButton(ClientSewing)
        self.pushButton_6.setGeometry(QtCore.QRect(520, 30, 230, 50))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.newSewing)

        QtCore.QMetaObject.connectSlotsByName(ClientSewing)

        self.pushButton_7 = QtWidgets.QPushButton(ClientSewing)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 30, 230, 50))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.deleteSewing)

        self.retranslateUi(ClientSewing)

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE') #подключаем базу данных с клиентами
        db.setDatabaseName('sewdb.db')
        db.open()

        query = QtSql.QSqlQuery('sewdb.db') # создание запроса

        query.exec_("create table sewing (ФИО varchar(50))") # задаем столбцы таблице sewing
        query.exec_("alter table sewing add Мобильный_телефон varchar(11)")
        query.exec_("alter table sewing add Электронная_почта varchar(50)")
        query.exec_("alter table sewing add Услуга varchar(50)")
        query.exec_("alter table sewing add Снятые_мерки varchar(100)")
        query.exec_("alter table sewing add Материал varchar(50)")
        query.exec_("alter table sewing add Фурнитура varchar(50)")
        query.exec_("alter table sewing add Колво_фурнитуры varchar(6)")
        query.exec_("alter table sewing add Крайний_срок varchar(10)")
        query.exec_("alter table sewing add Статус varchar(15)")
        query.exec_("alter table sewing add Цена varchar(10)")

        self.model = QtSql.QSqlTableModel()
        self.model.setTable('sewing')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()

        self.tableView.setModel(self.model)
        self.tableView.setWindowTitle("sewing")
        self.tableView.setItemDelegate(ReadOnlyDelegate())

        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)# разрешить выделение только по строкам

        query.exec_("select rowid, * FROM sewing")

        self.tableView.doubleClicked.connect(self.editSewing)# сигнал срабатывающий при двойном клике на tableView
    def newSewing(self): # функция создания новой записи
        self.newsew = Ui_NewSewing(self.model)
        self.newsew.show()

    def editSewing(self): # функция редактирования записи
        self.l = listService()
        try:
            currIndex = self.tableView.currentIndex()
            data = []
            for column in range(self.model.columnCount()):
                item = self.model.index(currIndex.row(), column).data()
                if item is None:
                    data.append("")
                else:
                    data.append(item)
            self.editsew = Ui_EditSewing(self.model, data, currIndex)
            self.editsew.show()
        except Exception as e:
            print(e)

    def newSearch(self):  # функция открывающая окно поиска
        self.newsew = Ui_search(self.model, self.tableView)
        self.newsew.show()

    def deleteSewing(self): # функция удаления записи
        query = QtSql.QSqlQuery('sewdb.db')
        indices = self.tableView.selectedIndexes()
        for index in sorted(indices):
            self.model.deleteRowFromTable(index.row())
        self.model.select()

    def makeLabel(self): # функция создания бирки
        from os import mkdir
        from os.path import isdir
        indices = self.tableView.selectedIndexes()
        if indices==[]:
            QMessageBox.about(self, "Ошибка", "Выберите запись!")
        for i in indices:
            data = []
            for column in range(self.model.columnCount()):
                item = self.model.index(i.row(), column).data()
                if item is None:
                    data.append("")
                else:
                    data.append(item)
            try:
                newLabel = Label(fio=str(data[0]), service=str(data[3]), furniture=str(data[6])+' '+str(data[7])+' шт', metrics=str(data[4]), deadline=str(data[8]),
                                 price=str(data[10]))

                if not isdir("./printing/"):
                    mkdir("./printing/")

                newLabel.getLabel().save(f"./printing/{data[0]} {data[3]} {data[8]}.png")
            except Exception as e:
                print(e)

    def retranslateUi(self, ClientSewing):
        _translate = QtCore.QCoreApplication.translate
        ClientSewing.setWindowTitle(_translate("ClientSewing", "Заказы. Пошив"))
        self.pushButton_4.setText(_translate("ClientSewing", "Поиск"))
        self.pushButton_5.setText(_translate("ClientSewing", "Создать бирку"))
        self.pushButton_6.setText(_translate("ClientSewing", "Новая запись"))
        self.pushButton_7.setText(_translate("ClientSewing", "Удалить"))

