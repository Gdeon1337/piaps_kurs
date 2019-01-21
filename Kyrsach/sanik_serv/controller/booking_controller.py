from sanic import Blueprint
from sanic.response import json
from service import booking_service


bp_booking = Blueprint('booking', url_prefix='/booking')


@bp_booking.route('/create_booking', methods=['GET'])
async def bp_create_user(request):
    booking = {
        'reader_id': request.args.get('reader_id'),
        'book_id': request.args.get('book_id'),
        'date_begin': request.args.get('date_begin'),
        'date_end': request.args.get('date_end'),
        'price': int(request.args.get('price'))
    }
    if booking.get('reader_id') is None or booking.get('book_id') is None or booking.get('date_begin') is None or \
            booking.get('date_end') is None or booking.get('price') is None:
        return json({'error': 'не все параметры указаны'})
    return json(await booking_service.create_booking(booking))


@bp_booking.route('/get_list_booking', methods=['GET'])
async def bp_create_user(request):
    reader_id = request.args.get('reader_id')
    if reader_id is None:
        return json({'error': 'не все параметры указаны'})
    return json(await booking_service.get_booking_list(int(reader_id)))


@bp_booking.route('/del_booking', methods=['GET'])
async def bp_create_user(request):
    booking_id = request.args.get('booking_id')
    if booking_id is None:
        return json({'error': 'не все параметры указаны'})
    return json(await booking_service.del_booking(int(booking_id)))
