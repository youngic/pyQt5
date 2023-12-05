import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from hello import Ui_MainWindow

class Test(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication([])          # 每个PyQt5应用都必须创建一个QApplication实例

    window = QWidget()              # 创建了一个QWidget实例，这是所有用户界面对象的基类
                                    # 可以把它当作一个窗口，我们可以在上面添加其他的 PyQt5 部件
    window.setWindowTitle('Simple PtQt5 App')
    window.show()                   # 设置窗口的标题，然后使用show方法来显示窗口

    app.exec_()                     # 进入应用的主循环，app.exec_()方法会启动主循环，直到exit()被调用或者主窗口被关闭

if __name__ == '__main__':
    # main()

    app = QApplication([])
    # window = QWidget()
    window = Test()
    window.show()
    app.exec_()