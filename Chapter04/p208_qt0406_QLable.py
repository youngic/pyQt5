from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap, QPalette

import sys


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()

        def link_hovered():
            print("当鼠标滑过label2标签时，触发事件")
        def link_clicked():
            print("当鼠标点击label4标签时，触发事件")

        Label1 = QLabel(self)
        Label2 = QLabel(self)
        Label3 = QLabel(self)
        Label4 = QLabel(self)

        #1 初始化标签控件
        Label1.setText("这是一个文本标签")
        Label1.setAutoFillBackground(True)                  # 自动填充背景
        palette = QPalette()                                # 调色板
        palette.setColor(QPalette.Window, Qt.blue)          # 蓝色背景
        Label1.setPalette(palette)
        Label1.setAlignment(Qt.AlignCenter)                 # 居中

        Label2.setText("<a href='#'>欢迎使用python gui应用</a>")                 # 
        
        Label3.setAlignment(Qt.AlignCenter)                       # 居中
        Label3.setToolTip("这是一个图片标签")                       # 提示
        Label3.setPixmap(QPixmap("d:/ui/subWin/pic/001.png"))      

        Label4.setText("<A href='www.baidu.com'>百度一下，你就知道</A>")        # 超链接
        Label4.setAlignment(Qt.AlignRight)
        Label4.setToolTip("这是一个超链接标签")

        #2 在窗口布局中添加控件
        vbox = QVBoxLayout()
        vbox.addWidget(Label1)
        vbox.addStretch()
        vbox.addWidget(Label2)
        vbox.addStretch()
        vbox.addWidget(Label3)
        vbox.addStretch()
        vbox.addWidget(Label4)

        #3 允许label1控件访问超链接
        Label1.setOpenExternalLinks(True)       # 允许打开访问超链接，默认不允许
        Label4.setOpenExternalLinks(False)      # 不允许打开超链接
        # 点击文本框绑定槽事件
        Label4.linkActivated.connect(link_clicked)

        # 划过文本框绑定槽事件
        Label2.linkActivated.connect(link_hovered)
        Label1.setTextInteractionFlags(Qt.TextSelectableByMouse)        # 文本可选

        self.setLayout(vbox)                    # 设置窗口布局
        self.setWindowTitle("QLabel1 案例")

     

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec())
    

