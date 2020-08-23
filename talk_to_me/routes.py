from flask import current_app as app, render_template, request, jsonify
from .models import User, Message, Chat
from . import db

@app.route('/chat/<int:chat_id>')
def chat(chat_id):
    m = Message.query.filter_by(chat=chat_id).order_by(db.desc(Message.id)).limit(10)
    print(type(m))
    messages = []
    for message in m:
        _m = {'id':message.id, 'chat':message.chat, 'sender':message.sender, 'content':message.content, 'timestamp':message.timestamp}
        messages.append(_m)
    print(messages[::-1])
    return render_template('chat.html', messages=messages[::-1], chat=chat_id)

@app.route('/message/<int:chat_id>', methods=['POST'])
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

@app.route('/message/<int:chat_id>', methods=['GET'])
def getMessages(chat_id):
    m = Message.query.filter_by(chat=chat_id).order_by(db.desc(Message.timestamp)).limit(10)
    dictm = {}
    for message in m:
        _m = {'id':message.id, 'chat':message.chat, 'sender':message.sender, 'content':message.content, 'timestamp':message.timestamp}
        print(_m)
        dictm[message.id] = _m
    print(jsonify(dictm))
    return jsonify(dictm), 200

# route to get latest 50 messages
# route to add new message to chat
# home/start chat route











@app.route('/wuggob')
def wuggob():
    return render_template('wuggob.html')