from rest_framework import viewsets
from rest_framework.response import Response
from .models import Detail
from .serializers import DetailSerializer


class DetailViewSet(viewsets.ModelViewSet):
    serializer_class = DetailSerializer

    def get_queryset(self):
        queryset = Detail.objects.all().order_by('-id')
        name = self.request.query_params.get('name')
        date = self.request.query_params.get('date')

        if name:
            queryset = queryset.filter(name__contains=name)
        elif date:
            queryset = queryset.filter(date=date)
        return queryset
