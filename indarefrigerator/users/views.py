from flask import Blueprint, redirect, render_template, request

from flask.ext.login import current_user, login_required, login_user, logout_user

from .forms import LoginForm


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect('/')
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login_user(form.user)
        return redirect('/')
    return render_template('index.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
