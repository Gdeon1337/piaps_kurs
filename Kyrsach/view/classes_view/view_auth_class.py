from PyQt5 import QtWidgets
from requests import Session
from view.model_view import view_vhod
from .view_reg_class import ClassRegistration
from .view_main_class import ClassMain


class ClassAuthorize(QtWidgets.QMainWindow, view_vhod.Ui_MainWindow):
    def __init__(self):
        self.secondWin = None
        super().__init__()
        self.session = Session()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.button_sigin.clicked.connect(self.check_text_box)
        self.button_signup.clicked.connect(self.open_registration_win)

    def check_text_box(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        if login is '' or password is '':
            self.statusBar().showMessage('Ошибка: логин или пароль отстутсвуют')
        else:
            response = self.session.get('http://0.0.0.0:8000/reader/authorize', params={
                'login': login,
                'password': password
            }).json()
            if response.get('error') is not None:
                self.statusBar().showMessage('Ошибка: логин или пароль неверные')
            else:
                self.session.cookies.update({'reader_id': str(response.get('id'))})
                if not self.secondWin:
                    self.secondWin = ClassMain(self.session)
                self.close()
                self.secondWin.show()

    def open_registration_win(self):
        if not self.secondWin:
            self.secondWin = ClassRegistration(self.session)
        self.close()
        self.secondWin.show()
