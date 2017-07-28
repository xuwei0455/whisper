# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask import request
from wechatpy.replies import TextReply
from wechatpy.replies import create_reply

from whisper.app.factory import AppFactory
from whisper.config import Config
from whisper.ext.wechat import wechat_required

app = AppFactory(__name__, Config)


@app.route('/wechat', methods=['GET', 'POST'])
@wechat_required
def wechat_handler():

    msg = request.wechat_msg

    if msg.type == 'text':
        reply = create_reply(msg.content, message=msg)
    else:
        reply = TextReply(content='hello', message=msg)

    return reply


if __name__ == '__main__':
    app.run(port=8080)