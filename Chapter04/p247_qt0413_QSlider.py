import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SliderDemo(QWidget):
    def __init__(self, parent=None):
        super(SliderDemo, self).__init__(parent)
        self.setWindowTitle("QSlider 案例")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.l1 = QLabel("Helllo PyQt5")            # TODO: 创建显示标签
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        
        self.sl = QSlider(Qt.Horizontal)        # 水平方向的滑动条
        self.sl.setMinimum(10)                  # 设置最小值
        self.sl.setMaximum(50)
        self.sl.setSingleStep(3)                # 设置步长

        self.sl.setValue(20)    # 设置当前值
        self.sl.setTickPosition(QSlider.TicksBelow)  # 设置刻度位置
        self.sl.setTickInterval(5)  # 设置刻度间隔

        layout.addWidget(self.sl)

        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(layout)

    def valuechange(self):
        print("当前值:%d" % self.sl.value())
        size = self.sl.value()
        self.l1.setFont(QFont("Times", size))       # TODO: 设置字体

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SliderDemo()
    demo.show()
    sys.exit(app.exec_())

