import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from p181_MainWin02 import Ui_Form
import p183_apprcc_rc


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 使用资源文件中的图像创建一个图标
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())


