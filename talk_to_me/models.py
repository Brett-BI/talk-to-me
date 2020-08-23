from datetime import datetime

from . import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat = db.Column(db.Integer, db.ForeignKey('chat.id'))
    sender = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=40))

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)