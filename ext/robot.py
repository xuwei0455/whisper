# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class ChatBotExt(object):

    def __init__(self, app=None):

        self._chatbot = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        self._chatbot = ChatBot(
            'ML-BOT',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch'
                },
                {
                    'import_path': 'chatterbot.logic.TimeLogicAdapter'
                },
                {
                    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.001,
                    'default_response': '我不明白你的意思....'
                }
            ],
        )
        self._chatbot.set_trainer(ChatterBotCorpusTrainer)
        self._chatbot.train(
            "chatterbot.corpus.chinese"
        )

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions['chatbot'] = self

    def __getattr__(self, name):
        return getattr(self._chatbot, name)

chatbot = ChatBotExt()
