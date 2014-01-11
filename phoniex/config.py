# -*- coding: utf-8 -*-

import os

from common import make_dir, INSTANCE_FOLDER_PATH

class BaseConfig(object):
    """
    Default configuration for a phoniex application
    """

    DEBUG = True

    SECRET_KEY = "secret"


    LOG_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'logs')
    make_dir(LOG_FOLDER)


    
    MAX_UPLOAD_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(INSTANCE_FOLDER_PATH, 'uploads')
    make_dir(UPLOAD_FOLDER)

class DefaultConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + INSTANCE_FOLDER_PATH + '/db.sqlite'

    #MYSQL for production.
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'


    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
# https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = DEBUG
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'yourmail@gmail.com'
    MAIL_PASSWORD = 'yourpass'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
