import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog
from PyQt5.uic.properties import QtGui
from requests import Session
from view.model_view import view_contract
import view.classes_view.view_profile_class
from docxtpl import DocxTemplate


class ClassContract(QtWidgets.QMainWindow, view_contract.Ui_MainWindow):
    def __init__(self, session: Session):
        super().__init__()
        self.secondWin = None
        self.list_id = -1
        self.session = session
        self.request = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_report.clicked.connect(self.report_my_doc)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.statusBar().showMessage('Для выбора договора жмите на ячейку ID')
        self.refresh_form()

    def refresh_form(self):
        self.request = self.session.get('http://0.0.0.0:8000/contract/get_list_contract',
                                        params={
                                            'reader_id': str(self.session.cookies.get('reader_id'))
                                        }).json()

        if isinstance(self.request, list):
            labels = ['ID', 'Книги', 'статус', 'Дата начала', 'Дата возврата', 'Стоимость']
            self.tableWidget.setColumnCount(len(labels))
            self.tableWidget.setHorizontalHeaderLabels(labels)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget.cellClicked.connect(self.cell_was_clicked)
            for contract in self.request:
                row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(row + 1)

                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(contract.get('id'))))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(contract.get('total_price'))))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(contract.get('status'))))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(contract.get('date_begin'))))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(contract.get('date_end'))))
                for book in contract.get('book_name'):
                    row = self.tableWidget.rowCount()
                    self.tableWidget.setRowCount(row + 1)
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(book))
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(''))
                    self.tableWidget.setItem(row, 5, QTableWidgetItem(''))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(''))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(''))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(''))

    def back(self):
        if not self.secondWin:
            self.secondWin = view.classes_view.view_profile_class.ClassProfile(self.session)
        self.close()
        self.secondWin.show()

    def report_my_doc(self):
        if self.list_id != -1:
            library_card = self.session.get('http://0.0.0.0:8000/reader/get_library_card',
                                            params={
                                               'reader_id': self.session.cookies.get('reader_id')
                                            }).json()
            reader_name = self.session.get('http://0.0.0.0:8000/reader/get_reader',
                                           params={
                                               'reader_id': self.session.cookies.get('reader_id')
                                            }).json()
            if library_card.get('error') is None and reader_name.get('error') is None:
                fname = QFileDialog.getSaveFileName(self, 'input')
                doc = DocxTemplate(os.path.dirname(__file__) + '/fopi.docx')
                contract_report = next((l for l in self.request if l['id'] == self.list_id), None)
                book_report = ''
                books = [book_name for book_name in contract_report.get('book_name')]
                for book in books:
                    book_report += ' ' + book
                context = {
                    'reader_name': reader_name.get('name'),
                    'contract_id': str(self.list_id),
                    'library_card_id': str(library_card.get('library_card_id')),
                    'total_price': contract_report.get('total_price'),
                    'date_begin': contract_report.get('date_begin'),
                    'date_end': contract_report.get('date_end'),
                    'books': book_report
                }
                doc.render(context)
                doc.save(fname[0] + "generated_doc.docx")
            else:
                self.statusBar().showMessage(library_card.get('error'))
        else:
            self.statusBar().showMessage('нужно что-то выбрать х_х')

    def cell_was_clicked(self, row, col):
        list_id_c = self.tableWidget.itemAt(col, row).text()
        contract_id = next((l for l in self.request if l['id'] == int(list_id_c)), None)
        if contract_id is None:
            self.statusBar().showMessage('Жмите на ячейку ID')
        else:
            self.list_id = contract_id.get('id')
