from sanik_serv.extensions import db


class Reader(db.Model):
    __tablename__ = 'reader'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000), nullable=False, unique=False)
    address = db.Column(db.String(1000), nullable=False, unique=False)
    sex = db.Column(db.String(1000), nullable=False, unique=False)
    passport = db.Column(db.String(1000), nullable=False, unique=False)
    age = db.Column(db.String(1000), nullable=False, unique=False)
    number_phone = db.Column(db.String(1000), nullable=False, unique=False)
    password = db.Column(db.String(1000), nullable=False, unique=False)
