from flask.ext.wtf import Form

from wtforms.ext.sqlalchemy.orm import model_form

from .models import Product


class ProductForm(model_form(Product, Form)):
    pass
