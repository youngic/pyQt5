import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class CheckBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(CheckBoxDemo, self).__init__(parent)

        groupBox = QGroupBox("Checkboxes")                  # 分组， 创建一个GroupBox控件
        groupBox.setFlat(True)  # 设置为平面的

        layout = QHBoxLayout()                              # 水平布局
        self.checkBox1 = QCheckBox("&Checkbox1")
        self.checkBox1.setChecked(True) # 设置为选中
        
        self.checkBox1.stateChanged.connect(lambda:self.btnstate(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox("Checkbox2")

        self.checkBox2.toggled.connect(lambda:self.btnstate(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox("Checkbox3")
        self.checkBox3.setTristate(True)                    # 设置为三态
        self.checkBox3.setCheckState(Qt.PartiallyChecked)   # 设置为部分选中
        
        self.checkBox3.stateChanged.connect(lambda:self.btnstate(self.checkBox3))
        layout.addWidget(self.checkBox3)
        
        groupBox.setLayout(layout)      # 设置布局


        mainLayout = QVBoxLayout()  # 垂直布局
        mainLayout.addWidget(groupBox)

        self.setLayout(mainLayout)  
        self.setWindowTitle("CheckBox Demo")

    def btnstate(self, btn):
        chk1States = self.checkBox1.text() + ", isChecked="+str(self.checkBox1.isChecked()) + ", checkState=" + str(self.checkBox1.checkState()) + "\n"
        chk2States = self.checkBox2.text() + ", isChecked="+str(self.checkBox2.isChecked()) + ", checkState=" + str(self.checkBox2.checkState()) + "\n"
        chk3States = self.checkBox3.text() + ", isChecked="+str(self.checkBox3.isChecked()) + ", checkState=" + str(self.checkBox3.checkState()) + "\n"
        print(chk1States + chk2States + chk3States)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    checkboxDemo = CheckBoxDemo()
    checkboxDemo.show()
    sys.exit(app.exec_())



