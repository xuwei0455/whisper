# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask import current_app as app


class SecretBase(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @staticmethod
    def async_run(func_name, *args, **kwargs):
        app.celery.send_task(func_name, args=args, kwargs=kwargs)

    def execute(self, **kwargs):
        """
        Every secret must can be execute
        :return:
        """
        raise NotImplementedError
