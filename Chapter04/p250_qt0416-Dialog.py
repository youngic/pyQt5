import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DialogDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("对话框案例")
        self.resize(350, 300)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showdialog)

    def showdialog(self):
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog test")
        dialog.setWindowModality(Qt.ApplicationModal)       # 窗口置顶
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DialogDemo()
    main.show()
    sys.exit(app.exec_())