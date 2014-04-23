from flask import Blueprint, render_template, request

from flask.ext.login import login_required

from .forms import ProductForm
from .models import Product
from ..extensions import db


product = Blueprint('product', __name__)


@product.route('/', methods=('GET', 'POST'))
@login_required
def index():
    model = Product()
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        form.populate_obj(model)
        db.session.add(model)
        db.session.commit()
        return 'ok'
    products = Product.query.order_by(Product.end_date).all()
    return render_template('products/index.html', form=form, products=products)
