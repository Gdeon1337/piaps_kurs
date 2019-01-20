from PyQt5 import QtWidgets
from requests import Session
from view.model_view import view_main
from .view_book_class import ClassBook


class ClassMain(QtWidgets.QMainWindow, view_main.Ui_MainWindow):
    def __init__(self, session: Session):
        super().__init__()
        self.secondWin = None
        self.session = session
        self.request = session.get('http://0.0.0.0:8000/book/get_list_book').json()
        self.setupUi(self)
        self.lineEditSearch.textEdited.connect(self.search_book_non)
        self.listWidget.itemClicked.connect(self.select_element_list)

    def search_book_non(self):
        self.listWidget.clear()
        name = self.lineEditSearch.text()
        list_search = []
        if name is not '':
            name = name.lower()
            for book in self.request:
                if str(book.get('name')).lower().find(name) is not -1 or\
                        str(book.get('author')).lower().find(name) is not -1:
                    list_search.append('' + book.get('name') + '_/_' + book.get('author') + '_/price:_'
                                       + str(book.get('price')))
        self.listWidget.addItems(list_search)

    def select_element_list(self, item):
        name = item.text()
        name = name.replace('price:', '')
        name = name.replace('_', '')
        list_book = name.split('/')
        for book in self.request:
            if book.get('name') == list_book[0] and book.get('author') == \
                    list_book[1] and book.get('price') == int(list_book[2]):
                if not self.secondWin:
                    response = self.session.get('http://0.0.0.0:8000/book/get_book', params={
                        'book_id': book.get('id')
                    }).json()
                    self.secondWin = ClassBook(response, self.session)
                self.close()
                self.secondWin.show()
