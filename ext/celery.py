# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from celery import Celery


class CeleryExt(object):

    def __init__(self, app=None):

        self._celery_client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        config = app.config
        config.setdefault('CELERY_BROKER_URL', None)

        assert config['CELERY_BROKER_URL'] is not None

        self._celery_client = Celery(
            app.import_name, broker=app.config['CELERY_BROKER_URL']
        )
        self._celery_client.conf.update(app.config)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['celery'] = self

    def __getattr__(self, name):
        return getattr(self._celery_client, name)


celery_ext = CeleryExt()
