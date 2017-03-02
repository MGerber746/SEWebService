from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from accounts import models as account_models
from accounts import serializers as account_serializers


class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = account_serializers.AccountSerializer

    def get_serializer_context(self):
        return {'token_id', Token.objects.get(user=self.request.user).pk}


class StudentViewSet(viewsets.ModelViewSet):
    queryset = account_models.Student.objects.all()
    serializer_class = account_serializers.StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = account_models.Teacher.objects.all()
    serializer_class = account_serializers.TeacherSerializer
