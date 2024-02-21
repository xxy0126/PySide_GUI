from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()

        button = QPushButton('按钮')
        button.clicked.connect(self.hello)  # clicked为信号

        mainlayout.addWidget(button)
        self.setLayout(mainlayout)

    def hello(self):
        print('Hello Word')

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec() 