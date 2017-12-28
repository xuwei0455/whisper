# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from whisper.app.secret.base import SecretBase
from whisper.ext.breeze import breeze
from whisper.ext.robot import chatbot


class Chat(SecretBase):

    def __init__(self, *args, **kwargs):
        self.msg = kwargs.get("msg", None)

        assert self.msg is not None

        kwargs.update({"flow_type": "text"})
        kwargs.update({"agent_id": self.msg.agent})
        kwargs.update({"user_id": self.msg.source})
        kwargs.update({"content": self.msg.content})

        super(Chat, self).__init__(*args, **kwargs)

    def execute(self, **kwargs):
        response = chatbot.get_response(kwargs["content"])
        kwargs["content"] = response.text
        breeze.flow(**kwargs)


if __name__ == '__main__':
    from flask import Flask
    from whisper.config import Config

    app = Flask(__name__)
    app.config.from_object(Config)
    chatbot.init_app(app)
    Chat().execute(**{"content": "english"})
