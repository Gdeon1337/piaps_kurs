from json import loads
from sanic import Blueprint
from sanic.response import json
from service import contract_service


bp_contract = Blueprint('contract', url_prefix='/contract')


@bp_contract.route('/create_contract', methods=['GET'])
async def bp_create_contract(request):
    contract = {
        'date_begin': request.args.get('date_begin'),
        'date_end': request.args.get('date_end'),
        'reader_id': request.args.get('reader_id'),
        'user_id': request.args.get('user_id'),
        'book': loads(request.args.get('book'))
    }
    if contract.get('date_begin') is None or contract.get('date_end') is None or contract.get('reader_id') is None \
            or contract.get('user_id') is None or contract.get('book') is None:
        return json({'error': 'не все параметры указаны'})
    return json(await contract_service.contract_add(contract))


@bp_contract.route('/get_list_contract', methods=['GET'])
async def search_book(request):
    if request.args.get('reader_id') is None:
        return json({'error': 'не все параметры указаны'})
    return json(
        await contract_service.get_list_contract(int(request.args.get('reader_id')))
    )
