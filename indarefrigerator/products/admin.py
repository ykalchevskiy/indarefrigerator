from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

from .models import Product
from ..extensions import admin, db


class ProductAdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_superuser()


admin.add_view(ProductAdminView(Product, db.session))
