# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算器.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(333, 306)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter_5 = QSplitter(Form)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Vertical)
        self.lineEdit = QLineEdit(self.splitter_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 80))
        self.lineEdit.setReadOnly(True)
        self.splitter_5.addWidget(self.lineEdit)
        self.splitter = QSplitter(self.splitter_5)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_7 = QPushButton(self.splitter)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.splitter.addWidget(self.pushButton_7)
        self.pushButton_8 = QPushButton(self.splitter)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.splitter.addWidget(self.pushButton_8)
        self.pushButton_9 = QPushButton(self.splitter)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.splitter.addWidget(self.pushButton_9)
        self.pushButton_division = QPushButton(self.splitter)
        self.pushButton_division.setObjectName(u"pushButton_division")
        self.splitter.addWidget(self.pushButton_division)
        self.splitter_5.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_5)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.pushButton_4 = QPushButton(self.splitter_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.splitter_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QPushButton(self.splitter_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.splitter_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.splitter_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.splitter_2.addWidget(self.pushButton_6)
        self.pushButton_multiplication = QPushButton(self.splitter_2)
        self.pushButton_multiplication.setObjectName(u"pushButton_multiplication")
        self.splitter_2.addWidget(self.pushButton_multiplication)
        self.splitter_5.addWidget(self.splitter_2)
        self.splitter_3 = QSplitter(self.splitter_5)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.pushButton_1 = QPushButton(self.splitter_3)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.splitter_3.addWidget(self.pushButton_1)
        self.pushButton_2 = QPushButton(self.splitter_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.splitter_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.splitter_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.splitter_3.addWidget(self.pushButton_3)
        self.pushButton_subtraction = QPushButton(self.splitter_3)
        self.pushButton_subtraction.setObjectName(u"pushButton_subtraction")
        self.splitter_3.addWidget(self.pushButton_subtraction)
        self.splitter_5.addWidget(self.splitter_3)
        self.splitter_4 = QSplitter(self.splitter_5)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.pushButton_0 = QPushButton(self.splitter_4)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.splitter_4.addWidget(self.pushButton_0)
        self.pushButton_dot = QPushButton(self.splitter_4)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.splitter_4.addWidget(self.pushButton_dot)
        self.pushButton_end = QPushButton(self.splitter_4)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.splitter_4.addWidget(self.pushButton_end)
        self.pushButton_add = QPushButton(self.splitter_4)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.splitter_4.addWidget(self.pushButton_add)
        self.splitter_5.addWidget(self.splitter_4)
        self.pushButton_back = QPushButton(self.splitter_5)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.splitter_5.addWidget(self.pushButton_back)
        self.pushButton_CE = QPushButton(self.splitter_5)
        self.pushButton_CE.setObjectName(u"pushButton_CE")
        self.splitter_5.addWidget(self.pushButton_CE)

        self.verticalLayout.addWidget(self.splitter_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_division.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_multiplication.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_subtraction.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_end.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"\u56de\u9000", None))
        self.pushButton_CE.setText(QCoreApplication.translate("Form", u"CE", None))
    # retranslateUi

