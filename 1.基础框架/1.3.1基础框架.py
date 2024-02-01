from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("来点击我呀",self)    # 创建按钮。并按钮设置为"来点击我呀"
        btn.setGeometry(100,100,200,100)    # 设置按钮所在的位置和大小
        btn.setToolTip('点我有惊喜')    # 设置鼠标放在按钮上的提示
        btn.setText('我被重新设置了')   # 重新设置按钮名称

        lb = QLabel('我是一个标签',self)    # 设置标签（文字）为”我是一个标签“
        lb.setText('我是被修改的文字')  # 重新设置标签内容
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter)   # 设置文字为居中效果

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec() 