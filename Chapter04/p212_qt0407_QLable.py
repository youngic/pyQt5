from PyQt5.QtWidgets import *
import sys

class QlabelDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel控件演示')
        nameLb1 = QLabel('&Name', self)
        nameEd1 = QLineEdit(self)
        nameLb1.setBuddy(nameEd1)               # 设置伙伴关系

        nameLb2 = QLabel('&Password', self)
        nameEd2 = QLineEdit(self)               # QLineEdit默认是不可编辑的
        nameLb2.setBuddy(nameEd2)               # 设置伙伴关系

        btnOK = QPushButton('&OK')              
        btnCancel = QPushButton('&Cannel')  
        mainLayout = QGridLayout(self)          # 创建网格布局
        mainLayout.addWidget(nameEd1, 0, 1, 1, 2)   # 添加控件

        mainLayout.addWidget(nameLb2, 1, 0)
        mainLayout.addWidget(nameEd2, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        def link_hovered(self):
            print("当鼠标滑过label2标签时，触发事件")

        def link_clicked(self):
            print("当鼠标点击label4标签时，触发事件")

        # 点击ok框绑定槽事件
        # btnOK.linkActivated.connect(link_clicked)
        btnOK.clicked.connect(link_clicked)
        # 点击cancel框绑定槽事件
        btnCancel.clicked.connect(link_hovered)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QlabelDemo()
    demo.show()
    sys.exit(app.exec_())
