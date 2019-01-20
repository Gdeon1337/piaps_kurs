from model.reader import Reader
from model.library_card import LibraryCard
from sanik_serv.extensions import db
from datetime import date
from dateutil.relativedelta import relativedelta


async def reader_add(reader: dict):
    async with db.transaction() as tx:
        check_reader = await Reader.query.where(Reader.number_phone == reader.get('number_phone') and
                                                Reader.passport == reader.get('passport')).gino.first()
        if check_reader is not None:
            return {'error': 'Такой пользователь уже существует'}
        reader = await Reader.create(
            name=reader.get('name'),
            address=reader.get('address'),
            sex=reader.get('passport'),
            age=reader.get('age'),
            number_phone=reader.get('number_phone'),
            password=reader.get('password'),
            passport=reader.get('passport'),
        )
        await LibraryCard.create(
            date=date.today().strftime('%d-%m-%Y'),
            term=(date.today() + relativedelta(months=+6)).strftime('%d-%m-%Y'),
            reader_id=reader.id
        )
        reader_dict = {
            'id': reader.id,
            'name': reader.name,
            'address': reader.address,
            'sex': reader.passport,
            'age': reader.age,
            'number_phone': reader.number_phone,
            'passport': reader.passport
        }
        return reader_dict


async def reader_get(reader_id):
    reader = await Reader.query.where(Reader.id == int(reader_id)).gino.first()
    if reader:
        reader_dict = {
            'name': reader.name,
            'address': reader.address,
            'sex': reader.passport,
            'age': reader.age,
            'number_phone': reader.number_phone,
            'passport': reader.passport
        }
        return reader_dict
    else:
        return {'error': 'Пользователь не найден'}


async def reader_authorize(reader_dict: dict):
    reader = await Reader.query.where(
        Reader.number_phone == reader_dict.get('login') and Reader.password == reader_dict.get('password')
    ).gino.first()
    if reader:
        reader_dict = {
            'id': reader.id,
            'name': reader.name,
            'address': reader.address,
            'sex': reader.passport,
            'age': reader.age,
            'number_phone': reader.number_phone,
            'passport': reader.passport
        }
        return reader_dict
    else:
        return {'error': 'Неверный логин или пароль'}
