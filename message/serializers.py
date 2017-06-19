from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class MessageSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        print(self.context['request'].content)
        validated_data['owner_id'] = self.context['request'].owner
        return Message.objects.create(**validated_data)