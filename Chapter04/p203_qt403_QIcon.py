import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication

#1 创建一个名为 Icon的窗口类，继承自Qwidget类
class Icon(QWidget):
    def __init__(self, parent=None):
        super(Icon, self).__init__(parent)
        self.initUI()
    
    #2 初始化窗口
    def initUI(self):
        self.setGeometry(300, 300, 230, 150)
        self.setWindowTitle("程序图标")
        self.setWindowIcon(QIcon('d:/ui/subWin/pic/002.png'))       # 图标路径


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Icon()
    ex.show()
    sys.exit(app.exec_())