from flask import Blueprint, current_app as app, render_template, request, jsonify, redirect, url_for
from flask_login import current_user

#from talk_to_me.models import Message, User, Chat
from talk_to_me import db

chat_bp = Blueprint('chat_bp', __name__, static_folder='static', static_url_path='/chat_bp/static/', template_folder='templates')

@chat_bp.route('/', methods=['GET'])
def home():
    return render_template('chat/home.html', current_user=current_user)


@chat_bp.route('/chat/<int:chat_id>')
def chat(chat_id):
    #m = Message.query(User, Message).filter_by(chat=chat_id).order_by(db.desc(Message.id)).limit(10)
    m = db.session.query(Message, User).join(User).filter(Message.chat==chat_id).order_by(db.desc(Message.id)).limit(10)
    print(m)
    print(type(m))
    messages = []
    for message in m:
        print(message[0].id)
        print(message[1].username)
        _m = {'id':message[0].id, 'chat':message[0].chat, 'sender':message[0].sender, 'username':message[1].username, 'content':message[0].content, 'timestamp':message[0].timestamp}
        messages.append(_m)
    print(messages[::-1])
    return render_template('chat/chat.html', messages=messages[::-1], chat=chat_id, current_user=current_user)


@chat_bp.route('/message/<int:chat_id>', methods=['POST'])
def sendMessage(chat_id):
    req = request.get_json()
    print(req['chat'])
    print(req['message'])
    print(req['user'])
    newMessage = Message(sender=req['user'], chat=req['chat'], content=req['message'])
    print(newMessage)
    db.session.add(newMessage)
    db.session.commit()
    return '', 201


@chat_bp.route('/message/<int:chat_id>', methods=['GET'])
def getMessages(chat_id):
    #m = Message.query.filter_by(chat=chat_id).order_by(db.desc(Message.timestamp)).limit(10)
    m = db.session.query(Message, User).join(User).filter(Message.chat==chat_id).order_by(db.desc(Message.id)).limit(10)
    dictm = {}
    for message in m:
        _m = {'id':message[0].id, 'chat':message[0].chat, 'sender':message[0].sender, 'username':message[1].username, 'content':message[0].content, 'timestamp':message[0].timestamp}
        print(_m)
        dictm[message[0].id] = _m
    print(jsonify(dictm))
    return jsonify(dictm), 200


@chat_bp.route('/chat/new', methods=['GET'])
def newChat():

    newChat = Chat()
    db.session.add(newChat)
    db.session.commit()

    return redirect(url_for('chat_bp.chat', chat_id=newChat.id))