from flask import Flask

from config import config_obj
from .manage import db
from application import api


app = Flask(__name__)
app.config.from_object(config_obj)


@app.errorhandler(404)
def not_found(error):
    return error


db.init_app(app)

api.api.init_app(app)
