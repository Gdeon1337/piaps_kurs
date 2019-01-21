from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from requests import Session
from view.model_view import view_booking_list
import view.classes_view.view_profile_class


class ClassBookingList(QtWidgets.QMainWindow, view_booking_list.Ui_MainWindow):
    def __init__(self, session: Session):
        super().__init__()
        self.secondWin = None
        self.list_id = -1
        self.session = session
        self.request = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_2.clicked.connect(self.delete_booking)
        self.refresh_form()

    def refresh_form(self):
        self.request = self.session.get('http://0.0.0.0:8000/booking/get_list_booking',
                                        params={
                                            'reader_id': str(self.session.cookies.get('reader_id'))
                                        }).json()

        if isinstance(self.request, list):
            labels = ['ID', 'Название книги', 'цена', 'Дата начала', 'Дата возврата']
            self.tableWidget.setColumnCount(len(labels))
            self.tableWidget.setHorizontalHeaderLabels(labels)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget.cellClicked.connect(self.cell_was_clicked)
            for booking in self.request:
                row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(row + 1)

                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(booking.get('id'))))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(booking.get('book_name')))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(booking.get('price'))))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(booking.get('date_end'))))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(booking.get('date_begin'))))

    def back(self):
        if not self.secondWin:
            self.secondWin = view.classes_view.view_profile_class.ClassProfile(self.session)
        self.close()
        self.secondWin.show()

    def cell_was_clicked(self, row):
        self.list_id = row

    def delete_booking(self):
        if self.list_id == -1 and self.request is not None:
            self.statusBar().showMessage('Ошибка: сначала нужно выбрать бронь')
        else:
            booking_id = str(self.request[self.list_id].get('id'))
            del_request = self.session.get('http://0.0.0.0:8000/booking/del_booking',
                                           params={
                                               'booking_id': booking_id
                                            }).json()
            if del_request.get('error') is None:
                self.tableWidget.clear()
                self.tableWidget.clearContents()
                self.refresh_form()
            else:
                self.statusBar().showMessage(del_request.get('error'))
