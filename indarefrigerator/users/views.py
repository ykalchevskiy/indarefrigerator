from flask import Blueprint, redirect, render_template, request, url_for

from flask.ext.login import current_user, login_required, login_user, logout_user

from .forms import LoginForm


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login', methods=['GET', 'POST'])
def login():
    redirect_url = request.args.get('next') or url_for('product.index')
    if current_user.is_authenticated():
        return redirect(redirect_url)
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user)
        return redirect(redirect_url)
    return render_template('index.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('product.index'))
