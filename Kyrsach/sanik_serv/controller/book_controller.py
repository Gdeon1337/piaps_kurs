from sanic import Blueprint
from sanic.response import json
from service import book_service


bp_book = Blueprint('book', url_prefix='/book')


@bp_book.route('/create_book', methods=['POST'])
async def add_book(request):
    book = {
        'name': request.args.get('name'),
        'author': request.args.get('author'),
        'genre': request.args.get('genre'),
        'price': request.args.get('price'),
        'date_zad': request.args.get('date_zad'),
        'img': request.form.get('img', ''),
        'description': request.form.get('description'),
    }
    if book.get('name') is None or book.get('author') is None or book.get('genre') is None or \
            book.get('price') is None or book.get('date_zad') is None or book.get('description') is None:
        return json({'error': 'не все параметры указаны'})
    return json(
        await book_service.create_book(book)
    )


@bp_book.route('/add_count_book', methods=['GET'])
async def add_count_book(request):
    arrival = {
        'count': request.args.get('count'),
        'book_id': request.args.get('book_id')
    }
    if arrival.get('count') is None or arrival.get('book_id') is None:
        return json({'error': 'не все параметры указаны'})
    return json(
        await book_service.add_count_book(arrival)
    )


@bp_book.route('/search_book', methods=['GET'])
async def search_book(request):
    name = request.args.get('search')
    if name is None:
        return json({'error': 'не все параметры указаны'})
    return json(
        await book_service.search(name)
    )


@bp_book.route('/get_list_book', methods=['GET'])
async def search_book(request):
    return json(
        await book_service.get_list()
    )


@bp_book.route('/get_book', methods=['GET'])
async def get_book(request):
    book_id = request.args.get('book_id')
    if book_id is None:
        return json({'error': 'не все параметры указаны'})
    return json(
        await book_service.get_book(book_id)
    )
