from flask import Blueprint

mod = Blueprint('hello', __name__)


@mod.route('/')
def hello_route():
    return 'hello'
