from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask.ext.login import current_user, login_required

from .forms import ProductForm
from .models import Product


product = Blueprint('product', __name__)


@product.route('/', methods=('GET', 'POST'))
@login_required
def index():
    model = Product()
    form = ProductForm(request.form)
    if form.validate_on_submit():
        form.populate_obj(model)
        model.save()
        flash('%r created!' % model)
        return redirect(url_for('product.index'))
    elif form.is_submitted():
        flash(form.errors)
    products = Product.query.order_by(Product.end_date).all()
    return render_template('products/index.html', form=form, products=products)


@product.route('/delete/<int:product_id>')
@login_required
def delete(product_id):
    model = Product.get_or_404(product_id)
    if current_user == model.user:
        flash('%r deleted!' % model)
        model.delete()
    return redirect(url_for('product.index'))
