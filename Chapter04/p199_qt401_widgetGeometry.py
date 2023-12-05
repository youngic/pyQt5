from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("Button")



# 以QWidget的左上角为原点
btn.move(20, 20)
# 不同操作系统可能对窗口的最小宽度有规定

widget.resize(300, 200)
widget.move(250, 200)

print('Qwidget: ')
print("w.x() = %d" % widget.x())
print("w.y() = %d" % widget.y())
print("w.width() = %d" % widget.width())
print("w.height() = %d" % widget.height())
print("QWidget.geometr")
print("widget.geometry().x() = %d" % widget.geometry().x())
print("widget.geometry().y() = %d" % widget.geometry().y())
print("widget.geometry().width() = %d" % widget.geometry().width())
print("widget.geometry().height() = %d" % widget.geometry().height())

widget.show()
sys.exit(app.exec_())
