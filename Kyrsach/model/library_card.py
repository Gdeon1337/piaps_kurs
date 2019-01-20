from sanik_serv.extensions import db


class LibraryCard(db.Model):
    __tablename__ = 'librarycard'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(), nullable=False, unique=False)
    term = db.Column(db.String(), nullable=False, unique=False)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
