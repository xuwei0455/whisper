# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from whisper.app.secret.base import SecretBase
from whisper.ext.breeze import breeze


class Echo(SecretBase):

    def __init__(self, *args, **kwargs):
        self.msg = kwargs.get("msg", None)

        assert self.msg is not None

        kwargs.update({"flow_type": "text"})
        kwargs.update({"agent_id": self.msg.agent})
        kwargs.update({"user_id": self.msg.source})
        kwargs.update({"content": self.msg.content})

        super(Echo, self).__init__(*args, **kwargs)

    def execute(self, **kwargs):
        breeze.flow(**kwargs)
