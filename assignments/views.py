from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from accounts.models import Teacher
from assignments.models import Assignment, Question
from assignments.serializers import AssignmentSerializer, QuestionSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    authentication_classes = [TokenAuthentication]

    def get_serializer_context(self):
        return {'request': self.request}

    def create(self, request, *args, **kwargs):
        return super(AssignmentViewSet, self).create(request, *args, **kwargs)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = [TokenAuthentication]

    def get_serializer_context(self):
        return {'request': self.request}
