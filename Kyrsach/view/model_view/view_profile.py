# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path/view_profile.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 161)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(150, 50, 211, 25))
        self.lineEdit_age.setReadOnly(True)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 10, 211, 25))
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 67, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 110, 191, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 110, 231, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 110, 201, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 60, 91, 17))
        self.label_7.setObjectName("label_7")
        self.lineEdit_number_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number_phone.setGeometry(QtCore.QRect(540, 10, 211, 25))
        self.lineEdit_number_phone.setReadOnly(True)
        self.lineEdit_number_phone.setObjectName("lineEdit_number_phone")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 10, 111, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(540, 50, 211, 25))
        self.lineEdit_password.setReadOnly(True)
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
        self.label.setText(_translate("MainWindow", "Фио"))
        self.label_2.setText(_translate("MainWindow", "Возраст"))
        self.pushButton.setText(_translate("MainWindow", "Просмотреть договоры"))
        self.pushButton_2.setText(_translate("MainWindow", "Просмотреть текущие брони"))
        self.pushButton_3.setText(_translate("MainWindow", "На главную"))
        self.label_7.setText(_translate("MainWindow", "Пароль"))
        self.label_5.setText(_translate("MainWindow", "Телефон/Логин"))

