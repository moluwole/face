import sys

import pymysql
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox

from face_capture import FaceCapture

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
        self.dte_dob.setDate(QtCore.QDate.currentDate())

    def classifier(self):
        student_name = self.txt_name.text()
        matric_num = self.txt_matric_num.text()
        address = self.txt_address.toPlainText()
        sex = str(self.cmb_sex.currentText())
        dept = str(self.cmb_dept.currentText())
        dob = self.dte_dob.date()
        dob = dob.toString("MM/dd/yyyy")

        if student_name == "" or matric_num == "" or address == "" or sex == "" or dept == "" or dob == "":
            QMessageBox.about(self, 'Error', 'Provide the student details to continue')
        else:
            sql = "Select * from student_details where matric_num=%s"
            cursor = connection.cursor()
            cursor.execute(sql, matric_num)
            result = cursor.fetchall()
            if int(len(result)) > 0:
                QMessageBox.about(self, 'Error', 'Student Details Exists Already in Database')
            else:
                sql = "Insert into student_details(name, matric_num, address, sex, dept, dob) Values(%s,%s,%s,%s,%s,%s)"
                cursor = connection.cursor()
                cursor.execute(sql, (student_name, matric_num, address, sex, dept, dob))
                connection.commit()
                FaceCapture(matric_num)
                QMessageBox.about(self, 'Success', 'Student Details Registered Successfully')

        # self.__get_face__ = GetFace()
        # self.__get_face__.__init__()
        # self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Register()
    window.show()
    sys.exit(app.exec_())
