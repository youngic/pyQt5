import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Radiodemo(QWidget):
    def __init__(self, parent = None):
        super(Radiodemo, self).__init__(parent)
        layout = QHBoxLayout()  # 创建水平布局
        self.btn1 = QRadioButton("Button1")
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda:self.btnstate(self.btn1))      
        layout.addWidget(self.btn1) # 将按钮添加到布局中

        self.btn2 = QRadioButton("Button2")
        self.btn2.toggled.connect(lambda:self.btnstate(self.btn2))
        layout.addWidget(self.btn2) # 将按钮添加到布局中

        self.setLayout(layout)  # 将布局添加到窗口
        self.setWindowTitle("Radiobutton_demo")

    def btnstate(self, btn):
        if btn.text()=="Button1":
            if btn.isChecked() == True:    
                print(btn.text()+"被选中")
            else:
                print(btn.text()+"未被选中")
        if btn.text()=="Button2":
            if btn.isChecked() == True:  
                print(btn.text()+"被选中")
            else:
                print(btn.text()+"未被选中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Radiodemo()
    demo.show()
    sys.exit(app.exec_())