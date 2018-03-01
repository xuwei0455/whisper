# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from random import randint

from flask import current_app as app

from whisper.app.secret.base import SecretBase
from whisper.ext.breeze import breeze
from whisper.ext.db import Poetry
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
        if kwargs["content"] == "来首诗":
            with app.app_context():
                poe_id = randint(1, 311828)
                poetry = Poetry.query.filter_by(id=poe_id).first()
                kwargs["content"] = poetry.title + "\n"
                kwargs["content"] += "\t\t" + poetry.author + "\n"
                kwargs["content"] += "\n".join(poetry.content.split("|"))
        else:
            response = chatbot.get_response(kwargs["content"])
            kwargs["content"] = response.text
        breeze.flow(**kwargs)


if __name__ == '__main__':
    from whisper.app.factory import AppFactory
    from whisper.config import Config

    app = AppFactory(app_name="f", conf_obj=Config)
    Chat().execute(**{"content": "来首诗"})
