import os

test_default_mysql = 'mysql://root:root@localhost:3306/bookameeting_test'

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'needs_to_be_changed'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URL = os.getenv('DEV_DATABASE_URL')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', test_default_mysql)
    SQLALCHEMY_TRACK_MODIFICATIONS = False



config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig
)