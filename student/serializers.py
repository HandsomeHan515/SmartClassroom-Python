from rest_framework import serializers
from django.db import models
from .models import Student, Classroom
from django.contrib.auth.models import User


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    classroom = serializers.StringRelatedField()
    duty = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = '__all__'
