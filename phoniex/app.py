# -*- coding: utf-8 -*- 

import os

from flask import Flask, render_template

from .config import DefaultConfig
from .extensions import db, cache, login_manager
from .common import INSTANCE_FOLDER_PATH


__all__ = ['create_app']

DEFAULT_BLUEPRINTS = ()

def create_app(config=None, app_name=None, blueprints=None):
    """create a flask app"""


    if app_name is None:
        app_name = DefaultConfig.PROJECT

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS


    app = Flask(app_name, instance_path = INSTANCE_FOLDER_PATH, instance_relative_config=True)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app£©

    return app



def configure_app(app, config=None):
    """
    Different ways of configurations.
    """


    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/config/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)

    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)

    #flask-cache
    cache.init_app(app)

    #flask-login
    login_manager.login_view = 'frontend.login'
    login_manager.refresh_view = 'frontend.reauth'
    login_manager.setup_app(app)


def configure_blueprints(app, blueprints):

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_template_filters(app):
    
    @app.template_filter()
    def pretty_date(value):
        return pretty_date(value)

    @app.template_filter()
    def format_date(value, format='%Y-%m-%d'):
        return value.strftime(format)

def configure_logging(app):
    """
    Configure file(info) and email(error) logging.
    """

    if app.debug or app.testing:
        return
 
    import logging
    from logging.handlers import SMTPHandler
 
    app.logger.setLevel(logging.INFO)
 
    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.hanlders.RotatingFileHandler(info_log, maxBytes=10000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
       '%(asctime)s %(levelname)s:%(message)s '
       '[in %(pathname)%: %(lineno)d]'
     ))

    app.logger.addHandler(info_file_handler)


    #Testing
    #app.logger.info('testing info')
    #app.logger.warn('testing warn')
    #app.logger.error('testing error')

    mail_handler = SMTPHandler(app.config['MAIL_SERVER'],
                               app.config['MAIL_USERNAME'],
			       app.config['ADMINS'],
			       'O_OPS ... %s failed!' % app.config['PROJECT'],
			       (app.config['MAIL_USERNAME'],
			        app.config['MAIL_PASSWORD']))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    ))

def configure_hook(app):
    @app.before_request
    def before_request():
        pass

def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("error/page_not_found.html"), 404

    @app.errorhandler(500):
    def server_error_page(error):
        return render_template("error/server_error.html"), 500
       
  
      
  
