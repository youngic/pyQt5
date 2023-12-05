import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SpinDemo(QWidget):
    def __init__(self, parent=None):
        super(SpinDemo, self).__init__(parent)
        self.setWindowTitle("SpinBox 案例")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.l1 = QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sp = QSpinBox()
        layout.addWidget(self.sp)
        
        self.sp.valueChanged.connect(self.valuechange)
        self.setLayout(layout)                              # 将布局添加到窗口

    def valuechange(self):
        self.l1.setText("curent value:" + str(self.sp.value()))     # 设置标签的文本

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpinDemo()
    ex.show()
    sys.exit(app.exec_())