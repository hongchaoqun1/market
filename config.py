import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET KEY') or 'hard to guess string'
    SQLALCHMY_COMMIT_ON_TEARDOWN = True
    FLASK_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    Debug = True
    #SQLALCHMY_DATABASE_URI = "xxx"   
    SQLALCHEMY_DATABASE_URI = 'xxx'     

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}            
