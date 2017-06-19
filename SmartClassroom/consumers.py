from student.models import Student
from channels import Group, Channel
from channels.sessions import channel_session

import json


@channel_session
def online_connect(message):
    message.reply_channel.send({"accept": True})


@channel_session
def online_receive(message):
    msg_dict = json.loads(message.content['text'])

    username = msg_dict['username']
    message.channel_session['username'] = username

    status = msg_dict['status']
    user_id = msg_dict['id']
    student = Student.objects.get(id=user_id)
    student.status = status
    student.save()


@channel_session
def online_disconnect(message):
    Group(username).discard(message.reply_channel)
