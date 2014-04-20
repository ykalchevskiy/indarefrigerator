from flask.ext.admin.contrib.sqla import ModelView

from .models import Product
from ..extensions import admin, db


admin.add_view(ModelView(Product, db.session))
