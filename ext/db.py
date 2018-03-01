# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Poetry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=False, nullable=False)
    author = db.Column(db.String(150), unique=False, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)

    def __repr__(self):
        return '<Poetry %r>' % self.id
