from sanik_serv.extensions import db


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=False)
    genre = db.Column(db.String(), nullable=False, unique=False)
    price = db.Column(db.Integer(), nullable=False, unique=False)
    author = db.Column(db.String(), nullable=False, unique=False)
    date_zad = db.Column(db.String(), nullable=False, unique=False)
    description = db.Column(db.String(), nullable=False, unique=False)
    img = db.Column(db.String())
