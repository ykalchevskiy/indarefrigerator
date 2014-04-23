from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

from .models import Product
from ..extensions import admin, db


class ProductAdminView(ModelView):
    def __init__(self, model, session, **kwargs):
        super(ProductAdminView, self).__init__(model, session, **kwargs)

    def is_accessible(self):
        return current_user.is_authenticated()


admin.add_view(ProductAdminView(Product, db.session))
