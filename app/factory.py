# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask import Flask

from whisper.ext.wechat import wechat
from whisper.ext.celery import celery_ext
from whisper.ext.breeze import breeze
from whisper.ext.robot import chatbot

__all__ = ["AppFactory"]

DEFAULT_APP_NAME = "Whisper"


class AppFactory(Flask):

    def __init__(self, app_name, conf_obj=None):
        if app_name is None:
            app_name = DEFAULT_APP_NAME
        super(AppFactory, self).__init__(app_name)

        app = self
        self.configure_app(app, conf_obj)
        self.configure_logger(app)
        self.configure_error_handlers(app)
        self.configure_extensions(app)
        self.configure_environment()
        self.configure_before_handlers(app)
        self.configure_after_handlers(app)

    @staticmethod
    def configure_app(app, config):

        if config is not None:
            app.config.from_object(config)

    @staticmethod
    def configure_before_handlers(app):
        """
        Authenticate is required before request.
        """
        pass

    @staticmethod
    def configure_after_handlers(app):
        """
        Authenticate is required after request.
        """
        pass

    @staticmethod
    def configure_extensions(app):
        wechat.init_app(app)
        celery_ext.init_app(app)
        breeze.init_app(app)
        chatbot.init_app(app)
        # api.init_app(app)
        # chat.init_app(app)
        # ldap_cli.init_app(app)
        # redis.init_app(app)
        pass

    @staticmethod
    def configure_environment():
        pass
        #
        # if BaseConfig.CHECK_IP_LIMIT:
        #     redis.master().hset("conf", "check_ip_limit", "true")
        # else:
        #     redis.master().hset("conf", "check_ip_limit", "false")

    @staticmethod
    def configure_error_handlers(app):

        if app.testing:
            return

    @staticmethod
    def configure_logger(app):
        #
        # logging.config.dictConfig(BaseConfig.LOGGING)

        if app.testing:
            return