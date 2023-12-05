import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.fontbtn = QPushButton("选择字体")
        self.fontbtn.clicked.connect(self.getFont)
        
        layout.addWidget(self.fontbtn)                  # 添加到表单布局
        self.fontLineEdit = QLabel("hello, 测试")
        layout.addWidget(self.fontLineEdit)             # 添加到表单布局

        self.setLayout(layout)
        self.setWindowTitle("Font Dialog 例子")

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = FontDialogDemo()
    dialog.show()
    sys.exit(app.exec_())