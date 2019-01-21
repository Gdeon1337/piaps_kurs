from sanik_serv.extensions import db
from .user import User


class Contract(db.Model):
    __tablename__ = 'contract'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(), nullable=False, unique=False)
    date_end = db.Column(db.String(), nullable=False, unique=False)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    status = db.Column(db.Boolean(), nullable=False, unique=False)
    total_price = db.Column(db.Integer(), nullable=False, unique=False)
