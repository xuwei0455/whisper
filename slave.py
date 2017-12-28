# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask import Flask

from whisper.config import Config
from whisper.ext.celery import celery_ext

app = Flask("celery_slave")
app.config.from_object(Config)

celery_ext.init_app(app)
celery = celery_ext
