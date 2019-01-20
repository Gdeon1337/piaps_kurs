from sanik_serv.extensions import db


class BookContract(db.Model):
    __tablename__ = 'bookcontract'

    id = db.Column(db.Integer(), primary_key=True)
    contract_id = db.Column(db.Integer, db.ForeignKey('contract.id'))
    price = db.Column(db.Integer(), nullable=False, unique=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    _contract = None

    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self, value):
        self._contract = value
