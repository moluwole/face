import sys

import pymysql
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from dashboard import Dashboard

# from PyQt4 import QtCore, QtGui, uic

connection = pymysql.connect(host='localhost', user='root', password='', db='face', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

qtCreatorFile = "login.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.__dashboard__ = None
        self.setupUi(self)

        self.btn_exit.clicked.connect(self.Exit)
        self.btn_login.clicked.connect(self.Login)

    def Login(self):
        username = self.txt_username.text()
        password = self.txt_pwd.text()
        if username == "" and password == "":
            QMessageBox.about(self, 'Error', 'Provide a Valid username and password to continue')
        else:
            cursor = connection.cursor()
            sql = "Select * from users where username=%s and pwd=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchall()
            if int(len(result)) <= 0:
                QMessageBox.about(self, "Error", "Invalid username and password. "
                                                 "Provide a valid username and password to continue ")
            else:
                self.__dashboard__ = Dashboard()
                self.__dashboard__.show()
                self.close()

    def Exit(self):
        reply = QMessageBox.question(self, "Exit?", "Would you like to exit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
            # sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    # window = test()
    window.show()
    sys.exit(app.exec_())
