from PyQt5.QtWidgets import QApplication, QLineEdit, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 例子")

        flo = QFormLayout()
        pIntLineEdit = QLineEdit()          # 整数
        pDoubleLineEdit = QLineEdit()       # 双精度
        pValidatorlineEdit = QLineEdit()    # 验证器

        flo.addRow("整数", pIntLineEdit)
        flo.addRow("双精度", pDoubleLineEdit)
        flo.addRow("验证器", pValidatorlineEdit)

        # 整型, 范围【1-99】
        pIntValidator = QIntValidator(self)                                # 创建验证器
        pIntValidator.setRange(1, 99)                                      

        # 双精度, 范围【-360, 360】
        pDoubleValidator = QDoubleValidator(self)                          # 创建验证器
        pDoubleValidator.setRange(-360, 360)         
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)    # TODO: 科学计数法
        pDoubleValidator.setDecimals(2)                                    # TODO: 保留两位小数

        # 字母和数字
        reg = QRegExp("[a-zA-Z0-9]+$")    # 只允许字母和数字
        pValidator = QRegExpValidator(self)                                # 创建验证器
        pValidator.setRegExp(reg)         # 设置正则表达式

        # 设置验证器
        pIntLineEdit.setValidator(pIntValidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorlineEdit.setValidator(pValidator)         

        self.setLayout(flo) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())