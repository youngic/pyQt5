import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.setWindowTitle("ComBox 案例")
        self.resize(300, 90)

        layout = QVBoxLayout()

        self.lbl = QLabel("")       # 创建标签
        self.cb = QComboBox()       # 创建下拉框
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        
        layout.addWidget(self.cb)       # 添加控件
        layout.addWidget(self.lbl)      # 添加控件
        self.setLayout(layout)

    def selectionchange(self, i):
        self.lbl.setText(self.cb.currentText())         # 设置标签的文本
        print("Items in the list are:") 
        for  count in range(self.cb.count()):
            print("Item" + str(count) + " = " + self.cb.itemText(count))
            print("Current index", i, "selecion changed", self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ComboxDemo()
    demo.show()
    sys.exit(app.exec_())