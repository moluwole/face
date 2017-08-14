import sys
from PyQt5 import QtWidgets, uic
from register import Register

qtCreatorFile = "dashboard.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Dashboard(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.__register__ = None
        self.__attendance____ = None

        self.btn_Register.clicked.connect(self.Register)
        # self.btn_Attendance.clicked.connect(self.Attendance)

    def Register(self):
        self.__register__ = Register()
        self.__register__.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard()
    # window = test()
    window.show()
    sys.exit(app.exec_())
