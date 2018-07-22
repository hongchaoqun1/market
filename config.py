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
    #SQLALCHMY_DATABASE_URI = "mysql+pymysql://root:root1root1@123@rm-bp15kq3103u1df435io.mysql.rds.aliyuncs.com:3306/wdblog?charset=utf8"   
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root1root1@123@rm-bp15kq3103u1df435io.mysql.rds.aliyuncs.com:3306/wdshop?charset=utf8'     

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