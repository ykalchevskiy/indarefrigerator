from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import current_user

from wtforms.fields import TextField

from .models import User
from ..extensions import admin, db


class UserAdminView(ModelView):
    column_list = ('email', 'is_admin')
    form_columns = ('email', 'is_admin')

    def scaffold_form(self):
        form_class = super(UserAdminView, self).scaffold_form()
        form_class.new_password = TextField('New password')
        return form_class

    def on_model_change(self, form, model, is_created):
        if form.new_password.data:
            model.password = form.new_password.data
        super(UserAdminView, self).on_model_change(form, model, is_created)

    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_superuser()


admin.add_view(UserAdminView(User, db.session))
