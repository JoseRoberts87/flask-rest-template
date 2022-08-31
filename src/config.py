import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG: bool = False
    TESTING: bool = False
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI: str = 'sqlite://'


class DevelopmentConfig(Config):
    ENV: str = 'development'
    DEBUG: bool = True
    TESTING: bool = True
    DEVELOPMENT: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite://'
    SECRET_KEY: str = 'development key'
    PREFERRED_URL_SCHEME: str = 'http'


class StagingConfig(Config):
    ENV: str = 'staging'
    DEBUG: bool = False
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite://'
    SECRET_KEY: str = 'development key'
    PREFERRED_URL_SCHEME: str = 'http'


class ProductionConfig(Config):
    ENV: str = 'production'
    DEBUG: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URI: str = 'sqlite://'
    SECRET_KEY: str = 'development key'
    PREFERRED_URL_SCHEME: str = 'http'


class TestingConfig(Config):
    ENV: str = 'testing'
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = 'sqlite://'
    SECRET_KEY: str = 'development key'
    PREFERRED_URL_SCHEME: str = 'http'
