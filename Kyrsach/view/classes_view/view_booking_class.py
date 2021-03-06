from PyQt5 import QtWidgets
from requests import Session
import view.classes_view.view_main_class
from view.model_view import view_booking
from datetime import date
from dateutil.relativedelta import relativedelta


class ClassBooking(QtWidgets.QMainWindow, view_booking.Ui_MainWindow):
    def __init__(self, book: dict, session: Session):
        self.secondWin = None
        super().__init__()
        self.setupUi(self)
        self.book = book
        self.session = session
        self.lineEdit.setText(book.get('name'))
        self.lineEdit_2.setText(book.get('author'))
        self.lineEdit_3.setText(str(book.get('price')))
        self.pushButton.clicked.connect(self.booking)
        self.pushButton_2.clicked.connect(self.back)
        self.dateTimeEdit.setMinimumDate(date.today())
        self.dateTimeEdit.setMaximumDate(date.today() + relativedelta(months=+6))
        self.dateTimeEdit_2.setMinimumDate(date.today())
        self.dateTimeEdit_2.setMaximumDate(date.today() + relativedelta(months=+6))
        self.dateTimeEdit.dateChanged.connect(self.date_price)
        self.dateTimeEdit_2.dateChanged.connect(self.date_price)

    def date_price(self):
        self.statusBar().clearMessage()
        if self.dateTimeEdit.date().toPyDate() == self.dateTimeEdit_2.date().toPyDate():
            day = 1
        else:
            day = self.dateTimeEdit.date().toPyDate() - self.dateTimeEdit_2.date().toPyDate()
            day = int(str(day).split()[0])
        if day < 0:
            self.statusBar().showMessage('Ошибка: Дата начала не может быть больше даты возврата')
        else:
            self.lineEdit_4.setText(str(self.book.get('price') * day))
            self.lineEdit_5.setText(str(day))

    def booking(self):
        day = self.dateTimeEdit.date().toPyDate() - self.dateTimeEdit_2.date().toPyDate()
        day = int(str(day).split()[0])
        if day < 0:
            self.statusBar().showMessage('Ошибка: Дата начала не может быть больше даты возврата')
        else:
            booking = {
                'reader_id': self.session.cookies.get('reader_id'),
                'book_id': self.book.get('id'),
                'date_begin': self.dateTimeEdit_2.date().toPyDate().strftime("%d %m, %Y"),
                'date_end': self.dateTimeEdit.date().toPyDate().strftime("%d %m, %Y"),
                'price': int(self.lineEdit_4.text())
            }
            response = self.session.get('http://0.0.0.0:8000/booking/create_booking', params=booking).json()
            if response.get('error') is not None:
                self.statusBar().showMessage(response.get('error'))
            else:
                if not self.secondWin:
                    self.secondWin = view.classes_view.view_main_class.ClassMain(self.session)
                self.close()
                self.secondWin.show()

    def back(self):
        if not self.secondWin:
            self.secondWin = view.classes_view.view_main_class.ClassMain(self.session)
        self.close()
        self.secondWin.show()
