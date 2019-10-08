import sqlite3
import sys

from qtpy import QtGui
from selenium import webdriver

import  module1 as m1
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtSql

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(400,100,400,400)
        self.setWindowTitle("instagram otomation")
        self.setWindowIcon(QtGui.QIcon('kfr.png'))

        newPersonalTxt = QtWidgets.QLineEdit(self)
        newPersonalTxt.resize(250,30)
        newPersonalTxt.move(50,10)

        newPersonal = QPushButton('add new personal', self)
        newPersonal.clicked.connect(self.clickPersonal)
        newPersonal.resize(100,32)
        newPersonal.move(50, 50)

        newGoal = QtWidgets.QLineEdit(self)
        newGoal.resize(250,30)
        newGoal.move(50,150)

        instagramAddFollewer = QRadioButton("Send Follewer ",self)
        instagramAddFollewer.resize(100,50)
        instagramAddFollewer.move(70,80)

        instagramSendLike = QRadioButton("Send Like",self)
        instagramSendLike.resize(100,50)
        instagramSendLike.move(70,110)

        newGoalBtn = QtWidgets.QPushButton("Goal ",self)
        newGoalBtn.clicked.connect(lambda :self.clickGoal(instagramAddFollewer.isChecked(),instagramSendLike.isChecked()))
        newGoalBtn.resize(100,32)
        newGoalBtn.move(50,190)

        Database = QtWidgets.QPushButton("database",self)
        Database.clicked.connect(self.clickDatabase)
        Database.resize(300,32)
        Database.move(50,292)



        self.personal = newPersonal
        self.personalTxt = newPersonalTxt
        self.newGoalTxt = newGoal
        self.newGoalBtn = newGoalBtn

    def clickPersonal(self):
        self.instagramPassword = "181172561121"
        databasename = "instagram-personal.db"
        attributes = "INSERT INTO instagramInformation (_USERNAME,_PASSWORD ) VALUES ('{}','{}')".format(self.personalTxt.text(),self.instagramPassword)
        m1.databaseInsertOperation(databasename, attributes)
        self.personalTxt.clear()

    def clickGoal(self,instagramAddFollewer,instagramSendLike):
        """
        con=sqlite3.connect("instagram-personal.db")
        cursor = con.cursor()
        cursor.execute("Select _USERNAME From instagramInformation ")
        liste = cursor.fetchall()
        print(liste[3][0])
        i=0
        for list in liste:
            print(liste[i][0])
            i+=1
        con.close()
        """

        instagramDatabase = "instagram-personal.db"
        instagramName = "Select _USERNAME From instagramInformation"
        if instagramSendLike:
            #buttonoperation
            buttonOperation = "/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button/span"
            m1.selenium_instagramAddFollewer(self.newGoalTxt.text(), instagramDatabase, instagramName, buttonOperation)

        if instagramAddFollewer:
            #buttonopereation
            buttonOperation = "/html/body/span/section/main/div/header/section/div[1]/div[1]/span/span[1]/button"
            m1.selenium_instagramAddFollewer(self.newGoalTxt.text(),instagramDatabase,instagramName,buttonOperation)

    def clickDatabase(self):
        self.SW = SecondWindow()
        self.SW.show()

class SecondWindow(QMainWindow):
        def __init__(self):
            super(SecondWindow, self).__init__()
            self.setGeometry(600, 100, 600, 400)
            self.setWindowTitle("database operation")
            self.setWindowIcon(QtGui.QIcon('kfr.png'))
            self.setUI()
            lbl = QLabel('Second Window', self)

        def databaseDB(self):

            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('instagram-personal.db')

            self.model = QtSql.QSqlTableModel()
            self.model.setTable("instagramInformation")
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0,Qt.Horizontal,'_ID')
            self.model.setHeaderData(1,Qt.Horizontal,'_NAME')
            self.model.setHeaderData(2, Qt.Horizontal, '_PASSWORD')

            view = QTableView()
            view.setModel(self.model)
            delrow = -1
            view.clicked.connect(self.satirAl)

            v_box = QVBoxLayout()

            btn2 = QPushButton('satirSil')


            btn2.clicked.connect(lambda : self.model.removeRow(view.currentIndex().row()))
            v_box.addWidget(view)

            v_box.addWidget(btn2)
            widget = QWidget()
            widget.setLayout(v_box)
            self.setCentralWidget(widget)

        def satirEkle(self):
            self.model.insertRowIntoTable(self.model.rowCount(),1)
        def satirAl(self,i):
            print(i.row())

        def setUI(self):
            self.databaseDB()
            self.show()


def databaseCreate():
    databasename = "instagram-personal.db"
    tablename = "instagramInformation"
    attributse = "(_ID INT,_USERNAME TEXT,_PASSWORD)"
    m1.database(databasename,tablename,attributse)

def main():
    app  = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    database = databaseCreate()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
