import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        self.pb.clicked.connect(self.qq)
        self.lb.setText('')
        self.q = 'Цвета: '
        self.g1 = QButtonGroup()
        self.g1.addButton(self.r11)
        self.g1.addButton(self.r12)
        self.g1.addButton(self.r13)
        self.g2 = QButtonGroup()
        self.g2.addButton(self.r21)
        self.g2.addButton(self.r22)
        self.g2.addButton(self.r23)
        self.g3 = QButtonGroup()
        self.g3.addButton(self.r31)
        self.g3.addButton(self.r32)
        self.g3.addButton(self.r33)

    def qq(self):
        if self.r11.isChecked():
            self.q += self.r11.text()
        if self.r12.isChecked():
            self.q += self.r12.text()
        if self.r13.isChecked():
            self.q += self.r13.text()
        if self.r21.isChecked():
            self.q += ', ' + self.r21.text()
        if self.r22.isChecked():
            self.q += ', ' + self.r22.text()
        if self.r23.isChecked():
            self.q += ', ' + self.r23.text()
        if self.r31.isChecked():
            self.q += ' и ' + self.r31.text()
        if self.r32.isChecked():
            self.q += ' и ' + self.r32.text()
        if self.r33.isChecked():
            self.q += ' и ' + self.r33.text()
        self.lb.setText(self.q)
        self.q = 'Цвета: '


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
