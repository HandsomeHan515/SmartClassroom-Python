from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def login(self, validated_data):
        print('validated_data', validated_data)
        username = validated_data['username']
        passwrod = validated_data['password']

        user = authenticate(username=username, passwrod=passwrod)
        if user is not None:
            print(user)
            return user
        else:
            print('Error')
