from flask import Flask

from .views import hello
from config import config_obj
from application.database import db
from application import api


app = Flask(__name__)
app.config.from_object(config_obj)


@app.errorhandler(404)
def not_found(error):
    return error


db.init_app(app)

app.register_blueprint(hello.mod, url_prefix="/hello")
api.api.init_app(app)
