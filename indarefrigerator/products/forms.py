from datetime import date, timedelta

from flask.ext.wtf import Form
from flask.ext.login import current_user

from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.fields import IntegerField, DateField
from wtforms.validators import Optional

from .models import Product
from ..extensions import db


class ProductForm(model_form(Product, db.session, Form)):
    life = IntegerField(validators=[Optional()])
    end_date = DateField(default=date.today, validators=[Optional()])

    def validate(self):
        life = self.life.data
        start_date = self.start_date.data
        end_date = self.end_date.data
        # no end_date
        if start_date and life and not end_date:
            self.end_date.data = start_date + timedelta(life)
        # no start_date
        if life and end_date and not start_date:
            self.start_date.data = end_date - timedelta(life)
        return super(ProductForm, self).validate()

    def populate_obj(self, obj):
        super(ProductForm, self).populate_obj(obj)
        obj.user = current_user
