from PyQt5 import QtWidgets
from requests import Session
from view.model_view import view_profile
import view.classes_view.view_main_class
from .view_booking_list_class import ClassBookingList
from .view_contract_class import ClassContract


class ClassProfile(QtWidgets.QMainWindow, view_profile.Ui_MainWindow):
    def __init__(self, session: Session):
        super().__init__()
        self.secondWin = None
        self.session = session
        self.request = self.session.get('http://0.0.0.0:8000/reader/get_reader',
                                       params={
                                           'reader_id': session.cookies.get('reader_id')
                                        }).json()
        self.setupUi(self)
        self.lineEdit_name.setText(self.request.get('name'))
        self.lineEdit_number_phone.setText(self.request.get('number_phone'))
        self.lineEdit_age.setText(self.request.get('age'))
        self.lineEdit_password.setText(self.request.get('password'))
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.create_win_bron)
        self.pushButton.clicked.connect(self.create_win_contract)

    def back(self):
        if not self.secondWin:
            self.secondWin = view.classes_view.view_main_class.ClassMain(self.session)
        self.close()
        self.secondWin.show()

    def create_win_bron(self):
        if not self.secondWin:
            self.secondWin = ClassBookingList(self.session)
        self.close()
        self.secondWin.show()

    def create_win_contract(self):
        if not self.secondWin:
            self.secondWin = ClassContract(self.session)
        self.close()
        self.secondWin.show()
