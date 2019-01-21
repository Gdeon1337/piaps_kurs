from sanic import Sanic, Blueprint
from .controller.reader_controller import bp
from .controller.book_controller import bp_book
from .controller.booking_controller import bp_booking
from .controller.contract_controller import bp_contract
from .controller.user_controller import bp_user
from .extensions import db


def create_app():
    app = Sanic(__name__.split('.')[0])
    register_blueprints(app)
    return app


def register_blueprints(app: Sanic):
    blueprint = Blueprint.group(bp, bp_book, bp_booking, bp_user, bp_contract)
    app.blueprint(blueprint)


async def register_extension():
    await db.set_bind('postgresql://gdeon1337:1337@localhost/gino4')
    await db.gino.create_all()
