from flask import Blueprint
from flask_restful import Api

from .views import Index, UserItem, UserItems

home_bp = Blueprint('home_bp', __name__)

home_api = Api(home_bp)

home_api.add_resource(Index, '/')
home_api.add_resource(UserItems, '/users')
home_api.add_resource(UserItem, '/users/<user_id>')
