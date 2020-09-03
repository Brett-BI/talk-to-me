from datetime import datetime

from flask_login import UserMixin

from . import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class DirectMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.Integer, db.ForeignKey('message.id'))


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)


class GroupMember(db.Model):
    group = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    member = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class GroupMessage(db.Model):
    group = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    message = db.Column(db.Integer, db.ForeignKey('message.id'), primary_key=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=40))

