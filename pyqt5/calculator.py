import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        self.setWindowTitle("Calculator App")
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon('pyqt5/icon.png'))
        self.setToolTip('my tooltip')
        self.initUI()

    def clicked(self):
        sender = self.sender().text()
        result = 0
        if sender == "Topla":
            result = int(self.txt_sayi.text()) + int(self.txt_sayi2.text())
        elif sender == "Çıkar":
            result = int(self.txt_sayi.text()) - int(self.txt_sayi2.text())
        elif sender == "Çarp":
            result = int(self.txt_sayi.text()) * int(self.txt_sayi2.text())
        elif sender == "Böl":
            result = int(self.txt_sayi.text()) / int(self.txt_sayi2.text())
        
        self.lbl_result.setText("Sonuç : " + str(result) )

    
    
    def initUI(self):
        self.lbl_sayi = QtWidgets.QLabel(self)
        self.lbl_sayi.setText("Sayi1: ")
        self.lbl_sayi.move(50,30)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi2:")
        self.lbl_sayi2.move(50,70)

        self.txt_sayi = QtWidgets.QLineEdit(self)
        self.txt_sayi.move(100,30)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(100,70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(150,270)
        self.lbl_result.resize(300,50)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Topla")
        self.btn_save.move(100,110)
        self.btn_save.clicked.connect(self.clicked)

        self.btn_save2 = QtWidgets.QPushButton(self)
        self.btn_save2.setText("Çıkar")
        self.btn_save2.move(100,150)
        self.btn_save2.clicked.connect(self.clicked)

        self.btn_save3 = QtWidgets.QPushButton(self)
        self.btn_save3.setText("Çarp")
        self.btn_save3.move(100,190)
        self.btn_save3.clicked.connect(self.clicked)

        self.btn_save4 = QtWidgets.QPushButton(self)
        self.btn_save4.setText("Böl")
        self.btn_save4.move(100,230)
        self.btn_save4.clicked.connect(self.clicked)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())

app()