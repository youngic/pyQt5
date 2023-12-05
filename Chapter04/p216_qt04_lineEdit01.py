from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys

class linEditDemo(QWidget):
    def __init__(self, parent=None):
        super(linEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 例子")

        flo = QFormLayout()
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()   # 无显示内容
        pPasswordLineEdit = QLineEdit()
        pPasswordEchoOnEditLineEdit = QLineEdit()

        flo.addRow("Normal", pNormalLineEdit)
        flo.addRow("NoEcho" , pNoEchoLineEdit)
        flo.addRow("Password", pPasswordLineEdit)
        flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEditLineEdit)

        pNormalLineEdit.setPlaceholderText("Normal")        # 占位文本
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("Password")
        pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置显示效果
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)   # 有显示内容
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)   # 无显示内容
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)   # 密码
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)   # 密码

        self.setLayout(flo)         # 设置布局

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = linEditDemo()
    demo.show()
    sys.exit(app.exec_())




