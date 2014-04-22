from flask.ext.wtf import Form

from wtforms.ext.sqlalchemy.orm import model_form
from wtforms.fields import IntegerField

from .models import Product


class ProductForm(model_form(Product, Form)):
    life = IntegerField()
