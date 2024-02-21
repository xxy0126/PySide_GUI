from PySide6.QtWidgets import QApplication, QWidget,QLineEdit,QVBoxLayout
from Ui_计算器 import Ui_Form   # 引入所制作的图形界面

class MyWindow(QWidget,Ui_Form):    # 同时也需要加载图形界面的类
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.result = ''    # 储存进行的步骤
        
        self.bind()     # 获取按键内容 

    # 设置按键功能
    def bind(self):
        self.pushButton_0.clicked.connect(lambda:self.addNUmber('0'))
        self.pushButton_1.clicked.connect(lambda:self.addNUmber('1'))
        self.pushButton_2.clicked.connect(lambda:self.addNUmber('2'))
        self.pushButton_3.clicked.connect(lambda:self.addNUmber('3'))
        self.pushButton_4.clicked.connect(lambda:self.addNUmber('4'))
        self.pushButton_5.clicked.connect(lambda:self.addNUmber('5'))
        self.pushButton_6.clicked.connect(lambda:self.addNUmber('6'))
        self.pushButton_7.clicked.connect(lambda:self.addNUmber('7'))
        self.pushButton_8.clicked.connect(lambda:self.addNUmber('8'))
        self.pushButton_9.clicked.connect(lambda:self.addNUmber('9'))
        self.pushButton_add.clicked.connect(lambda:self.addNUmber('+'))
        self.pushButton_subtraction.clicked.connect(lambda:self.addNUmber('-'))
        self.pushButton_multiplication.clicked.connect(lambda:self.addNUmber('*'))
        self.pushButton_division.clicked.connect(lambda:self.addNUmber('/'))
        self.pushButton_dot.clicked.connect(lambda:self.addNUmber('.'))
        self.pushButton_end.clicked.connect(self.equal)
        self.pushButton_CE.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.back)

    def addNUmber(self,number):
        self.lineEdit.clear     # 清除
        self.result += number   # 将当前的数字加入进去
        self.lineEdit.setText(self.result)     # 设置显示

    def equal(self):
        self.numberResult = eval(self.result)   # 计算数值
        self.lineEdit.setText(str(self.numberResult))   # 强制转化字符串,并且显示

    # 清空字符串
    def clear(self):
        self.result = ''
        self.lineEdit.clear()
    
    def back(self):
        self.result = self.result[:-1]      # 向左删除一个字符串
        self.lineEdit.setText(self.result)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec() 