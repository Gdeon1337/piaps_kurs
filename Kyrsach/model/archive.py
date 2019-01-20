from sanik_serv.extensions import db


class Archive(db.Model):
    __tablename__ = 'archive'

    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(1000), nullable=False, unique=False)
