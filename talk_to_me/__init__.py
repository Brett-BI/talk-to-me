from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///talk.db'
    app.config['SECRET_KEY'] = 'a4ab2cdef48df7b0104b3528'

    db.init_app(app)

    with app.app_context():
        from . import routes
        from .models import Message, User, Chat
        # db.create_all()

        # chat = Chat()
        # db.session.add(chat)
        # u1 = User(username="user1")
        # db.session.add(u1)
        # u2 = User(username="user2")
        # db.session.add(u2)
        # m1 = Message(chat="1", sender="1", content="Hi")
        # db.session.add(m1)
        # m2 = Message(chat="1", sender="2", content="Hey :)")
        # db.session.add(m2)
        # m3 = Message(chat="1", sender="1", content="How are you?")
        # db.session.add(m3)
        # m4 = Message(chat="1", sender="1", content="Tonight*")
        # db.session.add(m4)
        # m5 = Message(chat="1", sender="2", content="good")
        # db.session.add(m5)
        # db.session.commit()

        return app