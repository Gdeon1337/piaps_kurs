# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_vhod.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 195)
        MainWindow.setStyleSheet("Окно входа")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 67, 17))
        self.label_2.setObjectName("label_2")
        self.button_sigin = QtWidgets.QPushButton(self.centralwidget)
        self.button_sigin.setGeometry(QtCore.QRect(160, 120, 141, 41))
        self.button_sigin.setObjectName("button_sigin")
        self.button_signup = QtWidgets.QPushButton(self.centralwidget)
        self.button_signup.setGeometry(QtCore.QRect(0, 120, 151, 41))
        self.button_signup.setObjectName("button_signup")
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(80, 30, 221, 25))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 80, 221, 25))
        self.lineEdit_password.setObjectName("lineEdit_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.button_sigin.setText(_translate("MainWindow", "Войти"))
        self.button_signup.setText(_translate("MainWindow", "Зарегистрироваться"))

