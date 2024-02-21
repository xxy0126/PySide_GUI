from PySide6.QtWidgets import QApplication, QWidget,QLineEdit,QVBoxLayout
from login import Ui_Form   # 引入所制作的图形界面

class MyWindow(QWidget,Ui_Form):    # 同时也需要加载图形界面的类
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 点击名为self.pushButton的按钮时，会触发名为self.loginFuc的函数
        self.pushButton.clicked.connect(self.loginFuc) 

    def loginFuc(self):
        account = self.lineEdit.text()  # 获取账号,格式为"self.对象名.属性"
        password = self.lineEdit_2.text()    # 获取密码    
        
        # 制作登录判断功能
        if account == 'admin'and password == '123456':
            print('登录成功')
        else:
            print('登录失败')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec() 