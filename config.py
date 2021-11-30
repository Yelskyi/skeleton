import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "850a9d6c610aab4c473b41704e9832ee"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://test:Mysql8pass@localhost/test"


env_config = {
    "development": DevelopmentConfig
}

config_obj = env_config[os.environ.get("FLASK_ENV")]
