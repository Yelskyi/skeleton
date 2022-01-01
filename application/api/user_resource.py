from flask_restful import Resource, reqparse
from flask import request

from application.models import users


class UserResource(Resource):
    def get(self):
        data = users.Users.query.all()
        print(data)
        return "Users"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str)
        args = parser.parse_args()
        return args['user_id']
