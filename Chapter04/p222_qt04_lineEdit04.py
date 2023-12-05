from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont

import sys

class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())    # 整型
        e1.setMaxLength(4)                                  # TODO: 设置最大长度
        e1.setAlignment(Qt.AlignRight)       # 对齐方式
        e1.setFont(QFont("Arial", 20))       # 字体
        
        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))    #TODO: 双精度

        flo = QFormLayout()
        flo.addRow("interger validator", e1 )
        flo.addRow("double validator", e2 )

        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')

        flo.addRow("input mask", e3)

        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)        # 绑定槽函数， textchanged（）

        flo.addRow("text changed", e4)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)   # 密码

        flo.addRow("password", e5)

        e6 = QLineEdit("Hello")         # 设置默认内容
        e6.setReadOnly(True)            # 只读

        flo.addRow("read only", e6)

        e5.editingFinished.connect(self.enterPress)
        self.setLayout(flo)
        self.setWindowTitle("QLineEdit 例子")

    def textchanged(self, text):
        print("输入的内容为： "+text)

    def enterPress(self):
        print("输入完成")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lineEditDemo = lineEditDemo()
    lineEditDemo.show()
    sys.exit(app.exec_())