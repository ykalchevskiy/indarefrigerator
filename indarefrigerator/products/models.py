from datetime import date

from ..extensions import db
from ..users.models import User
from ..utils import CRUDModel


class Product(CRUDModel):
    __tablename__ = 'products'

    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Integer)
    amount_type = db.Column(db.String(255))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date, default=date.today, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship(User, backref=db.backref('products', lazy='dynamic'))

    METHODS = ['life', 'remaining']

    def life(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        return '-'

    def remaining(self):
        return (self.end_date - date.today()).days

    def __repr__(self):
        return '<Product %r up to %s>' % (self.name, self.end_date)
