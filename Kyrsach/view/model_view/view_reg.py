# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path/view_reg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(140, 20, 211, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(140, 60, 211, 25))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(140, 140, 211, 25))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.lineEdit_passport = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_passport.setGeometry(QtCore.QRect(140, 100, 211, 25))
        self.lineEdit_passport.setObjectName("lineEdit_passport")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(140, 230, 211, 25))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_number_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_phone.setGeometry(QtCore.QRect(140, 190, 211, 25))
        self.lineEdit_number_phone.setObjectName("lineEdit_number_phone")
        self.lineEdit_sex = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sex.setGeometry(QtCore.QRect(140, 270, 211, 25))
        self.lineEdit_sex.setObjectName("lineEdit_sex")
        self.pushButton_sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sign.setGeometry(QtCore.QRect(188, 320, 151, 25))
        self.pushButton_sign.setObjectName("pushButton_sign")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(10, 320, 161, 25))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 91, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 91, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 111, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 91, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 240, 91, 17))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_sign.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pushButton_back.setText(_translate("MainWindow", "Отмена"))
        self.label.setText(_translate("MainWindow", "Фио"))
        self.label_2.setText(_translate("MainWindow", "Возраст"))
        self.label_3.setText(_translate("MainWindow", "Пасспорт"))
        self.label_4.setText(_translate("MainWindow", "Адрес"))
        self.label_5.setText(_translate("MainWindow", "Телефон/Логин"))
        self.label_6.setText(_translate("MainWindow", "Пол"))
        self.label_7.setText(_translate("MainWindow", "Пароль"))

