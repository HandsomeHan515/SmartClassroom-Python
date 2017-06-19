from rest_framework import serializers
from .models import Detail
from django.contrib.auth.models import User


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'
