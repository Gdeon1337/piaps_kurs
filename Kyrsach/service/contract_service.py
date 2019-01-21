from model.contract import Contract
from model.book_contract import BookContract
from sanik_serv.extensions import db
from .book_service import get_list


async def contract_add(contract_dict: dict):
    async with db.transaction() as tx:
        contract = await Contract.create(
            date=contract_dict.get('date_begin'),
            date_end=contract_dict.get('date_end'),
            reader_id=int(contract_dict.get('reader_id')),
            user_id=int(contract_dict.get('user_id')),
            status=True,
            total_price=1
        )
        total_price = 0
        for book in contract_dict.get('book'):
            await BookContract.create(
                contract_id=contract.id,
                price=int(book.get('price')),
                book_id=int(book.get('book_id'))
            )
            total_price += int(book.get('price'))
        await contract.update(total_price=total_price).apply()
        return {'response': 'success'}


async def get_list_contract(reader_id: int):
    contract_list = await Contract.query.where(Contract.reader_id == reader_id).gino.all()
    book_contract_list = await BookContract.query.gino.all()
    book_list = await get_list()
    if contract_list is not None and book_list is not None:
        contract_dict = []
        for contract in contract_list:
            book_contracts = [l for l in book_contract_list if l.contract_id == contract.id]
            book_names = []
            for book_contract in book_contracts:
                book_names.append(next((l for l in book_list if l['id'] == book_contract.book_id), None).get('name'))
            contract_dict.append({
                'id': contract.id,
                'reader_id': contract.reader_id,
                'book_name': book_names,
                'date_begin': contract.date,
                'date_end': contract.date_end,
                'total_price': contract.total_price,
                'status': contract.status
            })
            return contract_dict
    else:
        return {'error': 'у вас ещё нет контрактов'}
