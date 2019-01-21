from PyQt5 import QtWidgets, QtCore
import base64
import view.classes_view.view_main_class
from PyQt5.QtGui import QPixmap
from requests import Session
from view.model_view import view_book
from .view_booking_class import ClassBooking


class ClassBook(QtWidgets.QMainWindow, view_book.Ui_MainWindow):
    def __init__(self, book: dict, session: Session):
        self.secondWin = None
        super().__init__()
        self.setupUi(self)
        self.book = book
        self.lineEdit.setText(self.book.get('name'))
        self.lineEdit_2.setText(self.book.get('author'))
        self.lineEdit_3.setText(self.book.get('genre'))
        self.lineEdit_4.setText(self.book.get('date_zad'))
        self.lineEdit_6.setText(str(self.book.get('price')))
        self.plainTextEdit.setPlainText(self.book.get('description'))
        if book.get('img') is not '':
            img = base64.b64decode(book.get('img'))
            pm = QPixmap()
            pm.loadFromData(img)
            self.label_img.setPixmap(pm.scaled(
                self.label_img.width(), self.label_img.height(), QtCore.Qt.KeepAspectRatio))
        self.pushButton.clicked.connect(self.booking)
        self.pushButton_2.clicked.connect(self.back)
        self.session = session

    def booking(self):
        response = self.session.get('http://0.0.0.0:8000/book/get_book', params={
            'book_id': self.book.get('id')
        }).json()
        if response.get('error') is not None:
            self.statusBar().showMessage(response.get('error'))
        else:
            if not self.secondWin:
                self.secondWin = ClassBooking(book=self.book, session=self.session)
            self.close()
            self.secondWin.show()

    def back(self):
        if not self.secondWin:
            self.secondWin = view.classes_view.view_main_class.ClassMain(session=self.session)
        self.close()
        self.secondWin.show()
