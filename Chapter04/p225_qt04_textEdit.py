from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys

class TextEditDemo(QWidget):
    def __init__(self,parent=None):
        super(TextEditDemo, self).__init__(parent)
        self.setWindowTitle("QTextEdit例子")
        self.resize(300, 270)
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("显示文本")
        self.btnPress2 = QPushButton("显示HTML")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)     # 将TextEdit控件添加到布局中
        layout.addWidget(self.btnPress1)    # 将PushButton控件添加到布局中
        layout.addWidget(self.btnPress2)    # 将PushButton控件添加到布局中

        self.setLayout(layout)              # 将布局添加到窗口

        self.btnPress1.clicked.connect(self.btnPress1_clicked)
        self.btnPress2.clicked.connect(self.btnPress2_clicked)

    def btnPress1_clicked(self):
            self.textEdit.setPlainText("Hello PyQt5! \n 单击按钮")

    def btnPress2_clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n单击按钮2。</font>")   # 设置文本为红色,字号为6, 并显示为HTML

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = TextEditDemo()
    demo.show()
    sys.exit(app.exec_())