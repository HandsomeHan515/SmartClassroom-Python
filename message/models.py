from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    owner = models.ForeignKey(User, related_name='message')
    content = models.TextField('信息内容')
    time = models.IntegerField('发布时间')

    def __str__(self):
        return self.content