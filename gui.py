import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyDialog(QWidget):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)

        layout = QVBoxLayout()
        self.btn = QPushButton("QFileDialog static method demo")
        self.btn.clicked.connect(self.getfile)

        layout.addWidget(self.btn)
        self.le = QLabel("Hello")

        # # layout.addWidget(self.le)
        # # self.btn1 = QPushButton("QFileDialog object")
        # # self.btn1.clicked.connect(self.getfiles)
        # # layout.addWidget(self.btn1)
        #
        # self.contents = QTextEdit()
        # layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        filename = fname[0]
        print filename
        self.le.setPixmap(QPixmap(filename))


def main():
    app = QApplication(sys.argv)
    ex = MyDialog()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
