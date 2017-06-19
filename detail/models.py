from django.db import models
from django.contrib.auth.models import User


class Detail(models.Model):
    name = models.CharField('姓名', max_length=16, null=True, blank=True)
    start = models.IntegerField('签到时间')
    duration = models.IntegerField('在线时长', blank=True, null=True)
    end = models.IntegerField('签退时间', blank=True, null=True)
    ip = models.GenericIPAddressField('登录IP')
    date = models.CharField('登录日期', max_length=16, null=True, blank=True)

    def __str__(self):
        return self.name