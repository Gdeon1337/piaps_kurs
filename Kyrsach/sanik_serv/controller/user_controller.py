from sanic import Blueprint
from sanic.response import json
from service import user_service


bp_user = Blueprint('user', url_prefix='/user')


@bp_user.route('/create_user', methods=['GET'])
async def bp_create_user(request):
    user = {
        'login': request.args.get('login'),
        'password': request.args.get('password')
    }
    if user.get('login') is None or user.get('password') is None:
        return json({'error': 'не все параметры указаны'})
    return json(await user_service.user_add(user))
