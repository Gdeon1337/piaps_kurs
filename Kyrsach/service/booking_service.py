from datetime import datetime

from model.book import Book
from model.book_contract import BookContract
from model.contract import Contract
from model.arrival import Arrival
from model.booking import Booking
from sanik_serv.extensions import db
from .book_service import get_list


async def create_booking(booking_dict: dict):
    async with db.transaction() as tx:
        book = await Book.query.where(Book.id == int(booking_dict.get('book_id'))).gino.first()
        if book is not None:
            arrival_list = await Arrival.query.gino.all()
            if arrival_list is None:
                return {'error': 'Нет в библиотеке'}
            count_list = await Arrival.select('count').where(Arrival.book_id ==
                                                             int(booking_dict.get('book_id'))).gino.scalar()
            if count_list is None:
                return {'error': 'Нет в библиотеке'}
            count_zan = await BookContract.load(
                contract=Contract.on(
                    BookContract.contract_id == Contract.id
                    and Contract.status
                    and BookContract.book_id == int(booking_dict.get('book_id')))).query.gino.all()
            count_booking = await db.func.count(Booking.book_id == int(booking_dict.get('book_id')) and
                                                datetime.strptime(Booking.date_begin, '%d-%m-%Y') <
                                                datetime.strptime(booking_dict.get('date_begin'), '%d-%m-%Y')
                                                < datetime.strptime(Booking.date_end, '%d-%m-%Y')).gino.scalar()
            count = count_list - len(count_zan) - count_booking
            if count <= 0:
                return {'error': 'Все разобрали, ждите когда вернут!'}
            await Booking.create(
                reader_id=int(booking_dict.get('reader_id')),
                book_id=int(booking_dict.get('book_id')),
                date_end=booking_dict.get('date_end'),
                date_begin=booking_dict.get('date_begin'),
                price=int(booking_dict.get('price'))
            )
            return {'response': 'success'}
        else:
            return {'error': 'Не найдёно'}


async def get_booking_list(reader_id: int):
    booking_list = await Booking.query.where(Booking.reader_id == reader_id).gino.all()
    book_list = await get_list()
    if booking_list is not None and book_list is not None:
        booking_dict = []
        for booking in booking_list:
            book_name = next((l for l in book_list if l['id'] == booking.book_id), None).get('name')
            booking_dict.append({
                'id': booking.id,
                'reader_id': booking.reader_id,
                'book_name': book_name,
                'date_begin': booking.date_begin,
                'date_end': booking.date_end,
                'price': booking.price,
                'book_id': booking.book_id
            })
        return booking_dict
    else:
        return {'error': 'у вас ещё нет броней'}


async def del_booking(booking_id: int):
    async with db.transaction() as tx:
        booking = await Booking.query.where(Booking.id == booking_id).gino.first()
        if booking is not None:
            await booking.delete()
            return {'response': 'success'}
        return {'error': 'уже нет такой брони'}
