from rest_framework import viewsets

from grades.models import Grade
from grades.serializers import GradeSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def get_serializer_context(self):
        return {'request', self.request}
