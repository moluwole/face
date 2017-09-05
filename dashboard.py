import sys

import pymysql
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from recognizer import Recognizer
from register import Register

qtCreatorFile = "dashboard.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
connection = pymysql.connect(host='localhost', user='root', password='', db='face', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class Dashboard(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.__register__ = None
        self.__attendance____ = None

        self.btn_Register.clicked.connect(self.Register)
        self.btn_Attendance.clicked.connect(self.Attendance)
        self.btnSearch.clicked.connect(self.Search)
        self.report_date.setDate(QtCore.QDate.currentDate())

        cursor = connection.cursor()
        sql = "Select * from attendance"
        cursor.execute(sql)

        result = cursor.fetchall()
        rows = len(result)
        if rows <= 0:
            QMessageBox.about(self, "No Data", "No Attendance has been recorded yet")
        else:
            self.tableWidget.setRowCount(rows)
            self.tableWidget.setColumnCount(3)
            header_labels = ['Matric Number', 'Date', 'Status']
            self.tableWidget.setHorizontalHeaderLabels(header_labels)

            for count in range(0, rows):
                self.tableWidget.setItem(count, 0,
                                         QTableWidgetItem(str(result[count]["matric_num"].encode('ascii', 'ignore'))))
                self.tableWidget.setItem(count, 1, QTableWidgetItem(result[count]["dte"].encode('ascii', 'ignore')))
                self.tableWidget.setItem(count, 2, QTableWidgetItem(result[count]["status"].encode('ascii', 'ignore')))



    def Register(self):
        self.__register__ = Register()
        self.__register__.show()
        self.close()

    def Attendance(self):
        Recognizer()

    def Search(self):
        matric_num = self.report_matric.text()
        search_date = self.report_date.date().toString("yyyy-MM-dd")

        if matric_num == "" and search_date == "":
            QMessageBox.about(self, "Invalid Parameters", "Please Provide a search Query to continue")
        else:
            self.tableWidget.setRowCount(0)
            if matric_num != "":
                sql = "Select * from attendance where matric_num = %s"
                cursor = connection.cursor()
                cursor.execute(sql, matric_num)
                result = cursor.fetchall()

            else:
                sql = "Select * from attendance where dte = %s"
                cursor = connection.cursor()
                cursor.execute(sql, search_date)
                result = cursor.fetchall()

            if len(result) > 0:
                self.tableWidget.setRowCount(len(result))
                self.tableWidget.setColumnCount(3)
                header_labels = ['Matric Number', 'Date', 'Status']
                self.tableWidget.setHorizontalHeaderLabels(header_labels)

                for count in range(0, len(result)):
                    self.tableWidget.setItem(count, 0, QTableWidgetItem(
                        str(result[count]["matric_num"].encode('ascii', 'ignore'))))
                    self.tableWidget.setItem(count, 1,
                                             QTableWidgetItem(result[count]["dte"].encode('ascii', 'ignore')))
                    self.tableWidget.setItem(count, 2,
                                             QTableWidgetItem(result[count]["status"].encode('ascii', 'ignore')))
            else:
                QMessageBox.about(self, "No Data", "No Data has been recorded")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard()
    # window = test()
    window.show()
    sys.exit(app.exec_())
