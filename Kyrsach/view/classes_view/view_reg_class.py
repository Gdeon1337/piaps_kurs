from view import classes_view
from PyQt5 import QtWidgets
from view.model_view import view_reg
from requests import Session
from .view_main_class import ClassMain


class ClassRegistration(QtWidgets.QMainWindow, view_reg.Ui_MainWindow):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.secondWin = None
        self.setupUi(self)
        self.pushButton_sign.clicked.connect(self.check_text_box)
        self.pushButton_back.clicked.connect(self.back)

    def check_text_box(self):
        reader = {
            'password': self.lineEdit_password.text(),
            'name': self.lineEdit_name.text(),
            'address': self.lineEdit_address.text(),
            'age': self.lineEdit_age.text(),
            'sex': self.lineEdit_sex.text(),
            'passport': self.lineEdit_passport.text(),
            'number_phone': self.lineEdit_number_phone.text()
        }
        if reader.get('name') is '' or reader.get('address') is '' or reader.get('passport') is '' or \
                reader.get('age') is '' or reader.get('number_phone') is '' or reader.get('password') is '' or \
                reader.get('sex') is '':
            self.statusBar().showMessage('Ошибка: Не все параметры написаны')
        else:
            response = self.session.get('http://0.0.0.0:8000/reader/create_reader', params=reader).json()
            if response.get('error') is not None:
                self.statusBar().showMessage('Ошибка:' + response.get('error'))
            else:
                #self.session.cookies.set(response)
                if not self.secondWin:
                    self.secondWin = ClassMain(self.session)
                self.close()
                self.secondWin.show()

    def back(self):
        if not self.secondWin:
            self.secondWin = classes_view.view_auth_class.ClassAuthorize()
        self.close()
        self.secondWin.show()
