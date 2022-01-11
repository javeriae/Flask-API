from datetime import datetime

from flask import request
from flask_restful import Resource

from .app import db
from .models import User
from .schemas import UserSchema
from .serializers import user_serializer


class Index(Resource):
    def get(self):
        return 'Server is up & running'


class UserItems(Resource):
    def get(self):
        users = User.query.all()
        results = [user_serializer(user) for user in users]
        return {
            'count': len(results),
            'objects': results,
        }

    def post(self):
        user_schema = UserSchema()
        errors = user_schema.validate(request.json)

        if errors:
            return {
               'error_msg': 'Invalid data.',
               'error_code': 'BAD_REQUEST',
               'status_code': 400
            }, 400

        user = User(
            name=request.json.get('name'),
            country=request.json.get('country'),
            active=request.json.get('active', False),
            created_on=datetime.utcnow(),
        )
        db.session.add(user)
        db.session.commit()

        return {
            'message': 'Record added successfully.',
            'resource_id': user.id,
            'status_code': 201
        }


class UserItem(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)

        if not user:
            return {
               'error_msg': 'Resource not found.',
               'error_code': 'NOT_FOUND',
               'status_code': 404
            }, 404

        return user_serializer(user)

    def put(self, user_id):
        user_schema = UserSchema()
        errors = user_schema.validate(request.json)

        if errors:
            return {
               'error_msg': 'Invalid data.',
               'error_code': 'BAD_REQUEST',
               'status_code': 400
            }, 400

        user = User.query.get(user_id)
        if user:
            user.name = request.json.get('name')
            user.country = request.json.get('country')
            user.active = request.json.get('active', False)

        db.session.add(user)
        db.session.commit()

        return {
            'message': 'Record updated successfully.',
            'resource_id': user.id,
            'status_code': 204
        }