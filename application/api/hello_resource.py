from flask_restful import Resource


class HelloResource(Resource):
    def get(self):
        return 123
