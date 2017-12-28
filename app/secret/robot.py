# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from whisper.app.secret.echo import Echo


class Robot(object):
    def __init__(self, msg):
        self.msg = msg

    def execute(self):
        index = self._msg_resolution()
        if not index:
            # todo: log
            return

        ins = self._secret_resolution()
        if not ins:
            # todo: log
            return

        return ins.execute(**ins.kwargs)

    @staticmethod
    def _msg_resolution():
        return 1

    def _secret_resolution(self):
        return Echo(msg=self.msg)
