from flask_restful import Api

from . import hello_resource, user_resource

api = Api(
    prefix="/api"
)

api.add_resource(hello_resource.HelloResource, '/hello-resource')
api.add_resource(user_resource.UserResource, "/get-users")
