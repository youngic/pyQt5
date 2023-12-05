import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        
        layout = QFormLayout()                  # 创建表单布局

        self.btn1 = QPushButton("获取列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()                  # 创建单行文本框
        layout.addRow(self.btn1, self.le1)      # 添加到表单布局

        self.btn2 = QPushButton("获取字符串")
        self.btn2.clicked.connect(self.getText)
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)      # 添加到表单布局

        self.btn3 = QPushButton("获取整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()  
        layout.addRow(self.btn3, self.le3)      # 添加到表单布局
        
        self.setLayout(layout)
        self.setWindowTitle("Input Dialog 例子")
    
    def getItem(self):
        items = ("C++", "Python", "Java", "C#")
        item, ok = QInputDialog.getItem(self, "select input dialog", "language", items, 0, False)   # 参数0指定最初选定项的索引，
                                                                                                    # 参数False禁用对话框中的可编辑文本字段
        if ok and item:
            self.le1.setText(item)      # 设置单行文本框的文本

    def getText(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', "输入姓名：")   # 获取文本
        if ok:
            self.le2.setText(str(text)) # 设置单行文本框的文本

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "interger input dialog", "输入数字")
        if ok:
            self.le3.setText(str(num))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = InputdialogDemo()
    win.show()
    sys.exit(app.exec_())

