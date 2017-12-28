# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from whisper.ext.celery import celery_ext


@celery_ext.task(name='w_send_text', ignore_result=True)
def w_send_text(breeze_client, **kwargs):
    """
    Send text message by wechat client
    """
    agent_id, user_id, content = kwargs.get("agent_id"), kwargs.get("user_id"), kwargs.get("content")
    breeze_client.message.send_text(agent_id, user_id, content)

