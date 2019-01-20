from sanik_serv.extensions import db


class Arrival(db.Model):
    __tablename__ = 'arrival'

    id = db.Column(db.Integer(), primary_key=True)
    count = db.Column(db.Integer(), nullable=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
