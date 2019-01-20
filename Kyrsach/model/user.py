from sanik_serv.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(1000), nullable=False, unique=False)
    password = db.Column(db.String(1000), nullable=False, unique=False)
