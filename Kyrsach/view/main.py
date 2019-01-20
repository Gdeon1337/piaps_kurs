import sys
from PyQt5 import QtWidgets
from view.classes_view.view_auth_class import ClassAuthorize


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ClassAuthorize()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
