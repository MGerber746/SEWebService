from rest_framework import viewsets

from classes.models import Class
from classes.serializers import ClassSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_serializer_context(self):
        return {'request': self.request}
