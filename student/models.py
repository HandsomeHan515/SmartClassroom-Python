from django.db import models
from django.contrib.auth.models import User


class Classroom(models.Model):
    name = models.CharField('班级名称', max_length=16)
    description = models.CharField('班级描述', max_length=32, blank=True)

    def __str__(self):
        return self.name


class Duty(models.Model):
    name = models.CharField('职务名称', max_length=16)
    description = models.CharField('职务描述', max_length=32, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS_CHOOSE = (
        (0, '离线'),
        (1, '在线'),
    )
    studentID = models.IntegerField('学号')
    name = models.ForeignKey(User)
    phone = models.IntegerField('电话号码', null=True, blank=True)
    email = models.EmailField('邮箱地址', null=True, blank=True)
    classroom = models.ForeignKey(Classroom)
    status = models.IntegerField('状态', choices=STATUS_CHOOSE)
    duty = models.ForeignKey(Duty, null=True, blank=True)

    def __str__(self):
        return self.name.username
