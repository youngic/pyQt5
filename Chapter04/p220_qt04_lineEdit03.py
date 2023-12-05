from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys

class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QlineEdit输入掩码的案例")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()  
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask('000.000.000.000;_')   # 设置输入掩码
        pMACLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')   # 设置输入掩码
        pDateLineEdit.setInputMask('0000-00-00')   # 设置输入掩码
        pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")   # 设置输入掩码

        flo.addRow("数字掩码", pIPLineEdit)
        flo.addRow("MAC掩码" , pMACLineEdit)
        flo.addRow("日期掩码", pDateLineEdit)
        flo.addRow("License掩码", pLicenseLineEdit)

        self.setLayout(flo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())