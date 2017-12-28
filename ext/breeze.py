# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from wechatpy.enterprise import WeChatClient


class Breeze(object):

    def __init__(self, app=None):

        self._breeze_client = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        config = app.config
        config.setdefault('WECHAT_APPID', None)
        config.setdefault('WECHAT_SECRET', None)

        assert config['WECHAT_APPID'] is not None
        assert config['WECHAT_SECRET'] is not None

        self._breeze_client = WeChatClient(
            app.config["WECHAT_APPID"], app.config["WECHAT_SECRET"])

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['breeze'] = self

    def flow(self, **kwargs):
        flow_type = kwargs.get("flow_type")

        if not flow_type:
            # todo: log
            return

        flow_method = getattr(self, "_flow_" + flow_type)
        if not flow_method:
            # todo: log
            return

        flow_method(**kwargs)

    def _flow_text(self, **kwargs):
        """
        # client.media.xxx()
        # client.tag.xxx()
        """
        from whisper.ext.celery import celery_ext
        celery_ext.send_task("w_send_text", args=(self._breeze_client, ), kwargs=kwargs)

        # agent_id, user_id, content = kwargs.get("agent_id"), kwargs.get("user_id"), kwargs.get("content")
        # self._breeze_client.message.send_text(agent_id, user_id, content)

breeze = Breeze()
