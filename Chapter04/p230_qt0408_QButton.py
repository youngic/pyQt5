import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()

        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)    # 设置按钮为可选中状态
        self.btn1.toggle()              # 设置初始状态为选中状态
        self.btn1.clicked.connect(lambda:self.whichbtn(self.btn1))  # 点击按钮触发事件
        self.btn1.clicked.connect(self.btnstate)  # 按钮状态改变触发事件
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton('image')
        self.btn2.setIcon(QIcon(QPixmap('d:/ui/subWin/pic/002.png')))
        self.btn2.clicked.connect(lambda:self.whichbtn(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)

        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda:self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)
        self.setWindowTitle("Button demo")

    def btnstate(self):
        if self.btn1.isChecked():
            print("button1 pressed")
        else:
            print("button1 released")
    
    def whichbtn(self, btn):
        print("clicked button is " + btn.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())