from model.book import Book
from model.book_contract import BookContract
from model.contract import Contract
from model.arrival import Arrival
from sanik_serv.extensions import db


async def create_booking(booking_dict: dict):
    book = await Book.query.where(Book.id == int(booking_dict.get('book_id'))).gino.first()
    if book is not None:
        count_list = await Arrival.query.select('count').where(Arrival.book_id is int(booking_dict.get('book_id')))\
            .gino.all()
        if count_list is None:
            return {'error': 'Нет на складе'}
        count_zan = await BookContract.load(
            contract=Contract.on(
                BookContract.contract_id == Contract.id and Contract.status)).where(BookContract.book_id == int(booking_dict.get('book_id'))).query.gino.all()
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
