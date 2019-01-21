from model.user import User
from sanik_serv.extensions import db


async def user_add(user: dict):
    async with db.transaction() as tx:
        check_user = await User.query.where(User.login == user.get('login') and
                                            User.password == user.get('password')).gino.first()
        if check_user is not None:
            return {'error': 'Такой пользователь уже существует'}
        await User.create(
            login=user.get('login'),
            password=user.get('password')
        )
        return {'response': 'success'}
