from sanic import Blueprint
from sanic.response import json
from service import reader_service


bp = Blueprint('reader', url_prefix='/reader')


@bp.route('/create_reader', methods=['GET'])
async def bp_create_user(request):
    reader = {
        'name': request.args.get('name'),
        'address': request.args.get('address'),
        'sex': request.args.get('sex'),
        'age': request.args.get('age'),
        'number_phone': request.args.get('number_phone'),
        'password': request.args.get('password'),
        'passport': request.args.get('passport')
    }
    if reader.get('name') is None or reader.get('address') is None or reader.get('passport') is None or \
            reader.get('age') is None or reader.get('number_phone') is None or reader.get('password') is None or\
            reader.get('sex') is None:
        return json({'error': 'не все параметры указаны'})
    return json(await reader_service.reader_add(reader))


@bp.route('/authorize', methods=['GET'])
async def bp_authorize(request):
    if request.args.get('login') is None or request.args.get('password') is None:
        return json({'error': 'не все параметры указаны'})
    return json(
        await reader_service.reader_authorize(
            {
                'login': request.args.get('login'),
                'password': request.args.get('password')
            }
        )
    )


@bp.route('/get_reader', methods=['GET'])
async def bp_get_reader(request):
    if request.args.get('reader_id') is None:
        return json({'error': 'не все параметры указаны'})
    return json(await reader_service.reader_get(request.args.get('reader_id')))
