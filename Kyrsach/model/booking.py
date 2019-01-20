from sanik_serv.extensions import db


class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer(), primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    date_end = db.Column(db.String(), nullable=False, unique=False)
    date_begin = db.Column(db.String(), nullable=False, unique=False)
    price = db.Column(db.Integer(), nullable=False, unique=False)
