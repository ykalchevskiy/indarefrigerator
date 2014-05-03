from flask import request

from flask.ext.login import current_user
from flask.ext.restful import Resource
from flask.ext.restless.helpers import strings_to_dates, to_dict

from .models import Product
from ..extensions import api, db


class ProductResource(Resource):

    def delete(self, product_id):
        instance = Product.query.get(product_id)
        db.session.delete(instance)
        db.session.commit()
        return {}

    def put(self, product_id):
        instance = Product.query.get(product_id)
        params = strings_to_dates(Product, request.form)
        for field, value in params.items():
            setattr(instance, field, value)
        db.session.commit()
        return to_dict(instance)


class ProductListResource(Resource):
    def post(self):
        params = strings_to_dates(Product, request.form)
        params.pop('life', None)
        params['user'] = current_user
        instance = Product(**params)
        db.session.add(instance)
        db.session.commit()
        return to_dict(instance)


api.add_resource(ProductResource, '/api/products/<int:product_id>')
api.add_resource(ProductListResource, '/api/products')
