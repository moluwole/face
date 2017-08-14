import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from get_face import Getface
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', db='face', charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
qtCreatorFile = "register.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Register(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.__get_face__ = None
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_train_classifier.clicked.connect(self.classifier)

    def classifier(self):
        student_name = self.txt_name.text()
        matric_num = self.txt.matric_num.text()
        address = self.txt_address.text()
        sex = self.cmb_sex.itemData(self.cmb_sex.currentIndex()).toPyObject()
        dob = self.dte_dob.date()

        sql = "Select * from student where matric_num=%s"
        cursor = connection.cursor()
        cursor.execute(sql, matric_num)
        result = cursor.fetchall()
        if int(len(result)) > 0:
            QMessageBox.about(self, 'Error', 'Student Details Exists Already in Database')
        else:
            sql = "Insert into student(name, matric_num, address, sex, dob) Values(%s,%s,%s,%s,%s)"
            cursor = connection.cursor()
            cursor.execute(sql, (student_name, matric_num, address, sex, dob))
            connection.commit()
            Getface("oluwole")
            QMessageBox.about(self, 'Success', 'Student Details Registered Successfully')

        # self.__get_face__ = GetFace()
        # self.__get_face__.__init__()
        # self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Register()
    window.show()
    sys.exit(app.exec_())
