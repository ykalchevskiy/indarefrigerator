from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask.ext.login import current_user, login_required

from .forms import ProductForm
from .models import Product


product = Blueprint('product', __name__)


@product.route('/old', methods=('GET', 'POST'))
@login_required
def index():
    model = Product()
    form = ProductForm(request.form)
    if form.validate_on_submit():
        form.populate_obj(model)
        model.save()
        flash('%r created!' % model.name, 'success')
        return redirect(url_for('product.index'))
    elif form.is_submitted():
        flash(form.errors, 'danger')
    products = Product.query.filter(Product.user == current_user).order_by(Product.end_date).all()
    return render_template('products/index.html', form=form, products=products)


@product.route('/old/delete/<int:product_id>')
@login_required
def delete(product_id):
    model = Product.get_or_404(product_id)
    if current_user == model.user:
        flash('%r deleted!' % model.name, 'success')
        model.delete()
    return redirect(url_for('product.index'))


@product.route('/')
@login_required
def ng():
    return render_template('products/ng.html')
