import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton("加载图片")

        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        self.le = QLabel("")
        layout.addWidget(self.le)

        self.btn1 = QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        
        self.setLayout(layout)

        self.setWindowTitle("File Dialog 例子")
    
    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, "open File", 'c:\\', "Image files(*.jpg *.gif)")   # 设置文件扩展名过滤,注意用双引号
        self.le.setPixmap(QPixmap(fname))       # 加载图片

    def getfiles(self):
        dlg = QFileDialog()                     # 创建QFileDialog对象
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)               # 设置文件过滤器只显示文件

        if dlg.exec_():
            filenames = dlg.selectedFiles()         # 返回文件名列表
            f = open(filenames[0], 'r')
            with f:                                 # TODO: 用于确保文件在打开后被正确关闭
                data = f.read()
                self.contents.setText(data)         # 读取文件内容，然后将文本设置未文本小部件self的内容


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())



