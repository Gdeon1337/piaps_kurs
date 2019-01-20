from model.book import Book
from model.arrival import Arrival
from sanik_serv.extensions import db


async def search(name: str):
    book_list = await Book.query.where(Book.name == name or Book.author == name).gino.all()
    if book_list is not None:
        book_dict = []
        for book in book_list:
            book_dict.append({
                'id': book.id,
                'name': book.name,
                'author': book.author,
                'genre': book.genre,
                'price': book.price,
                'date_zad': book.date_zad
            })
        return book_dict
    else:
        return {'error': 'Не найдёно'}


async def get_list():
    book_list = await Book.query.gino.all()
    if book_list is not None:
        book_dict = []
        for book in book_list:
            book_dict.append({
                'id': book.id,
                'name': book.name,
                'author': book.author,
                'genre': book.genre,
                'price': book.price,
                'date_zad': book.date_zad
            })
        return book_dict
    else:
        return {'error': 'в бд нет книг'}


async def create_book(book: dict):
    async with db.transaction() as tx:
        check_book = await Book.query.where(Book.name == book.get('name') and
                                            Book.author == book.get('author') and Book.genre == book.get('genre')
                                            and Book.price == book.get('price')).gino.first()
        if check_book is not None:
            return {'error': 'Такая книга уже существует'}
        await Book.create(
            name=book.get('name'),
            genre=book.get('genre'),
            price=int(book.get('price')),
            author=book.get('author'),
            date_zad=book.get('date_zad'),
            img=book.get('img'),
            description=book.get('description')
        )
        return {'response': 'success'}


async def add_count_book(book_arrival:dict):
    async with db.transaction() as tx:
        check_book = await Book.query.where(Book.id == book_arrival.get('book_id')).gino.first()
        if check_book is None:
            return {'error': 'Такой книги не существует'}
        await Arrival.create(
            count=book_arrival.get('count'),
            book_id=book_arrival.get('book_id')
        )
        return {'response': 'success'}


async def get_book(book_id: str):
    book = await Book.query.where(Book.id == int(book_id)).gino.first()
    if book is not None:
        book_dict = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'genre': book.genre,
            'price': book.price,
            'date_zad': book.date_zad,
            'img': book.img,
            'description': book.description
        }
        return book_dict
    else:
        return {'error': 'Не найдёно'}


async def get_book_in_booking(book_id: str):
    book = await Book.query.where(Book.id == int(book_id)).gino.first()
    if book is not None:
        count_list = await Arrival.query.select('count').where(Arrival.book_id is int(book_id)).gino.all()
        if count_list is None:
            return {'error': 'Нет на складе'}
        count = sum(count_list)
        if count <= 0:
            return {'error': 'Все разобрали, ждите когда вернут!'}
        book_dict = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'price': book.price,
            'count': count
        }
        return book_dict
    else:
        return {'error': 'Не найдёно'}
