from flask.ext.login import current_user
from flask.ext.restless import ProcessingException

from .models import Product
from ..extensions import api


def auth_preprocessor(*args, **kwargs):
    if not current_user.is_authenticated():
        raise ProcessingException(description='Not authenticated!', code=401)


def check_instance_user_preprocessor(instance_id=None, **kwargs):
    if not Product.get_or_404(instance_id).user == current_user:
        raise ProcessingException(description='Forbidden!', code=403)


def get_many_preprocessor(search_params=None, **kwargs):
    auth_filter = {'name': 'user', 'op': '==', 'val': current_user}
    search_params.setdefault('filters', []).append(auth_filter)


def post_preprocessor(data=None, **kwargs):
    data['user'] = current_user


def put_single_preprocessor(data=None, **kwargs):
    data.pop('life', None)
    data.pop('remaining', None)


api = api.create_api(Product,
                     include_methods=['life', 'remaining'],
                     methods=['GET', 'POST', 'PUT', 'DELETE'],
                     results_per_page=100,
                     preprocessors={
                         'GET_MANY': [auth_preprocessor, get_many_preprocessor],
                         'GET_SINGLE': [auth_preprocessor, check_instance_user_preprocessor],
                         'POST': [auth_preprocessor, post_preprocessor],
                         'PUT_SINGLE': [auth_preprocessor, check_instance_user_preprocessor, put_single_preprocessor],
                         'DELETE': [auth_preprocessor, check_instance_user_preprocessor]
                     })
