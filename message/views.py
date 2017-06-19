from .models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-id')
    serializer_class = MessageSerializer
