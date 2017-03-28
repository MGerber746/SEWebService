from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts import models as account_models
from accounts import serializers as account_serializers
from classes import serializers as class_serializers


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = account_serializers.AccountSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = account_models.Student.objects.all()
    serializer_class = account_serializers.StudentSerializer

    @list_route(['get'], authentication_classes=[TokenAuthentication],
                permission_classes=[IsAuthenticated], url_path="get-classes")
    def get_classes(self, request):
        student = account_models.Student.objects.get(user=request.user)
        classes = student.class_set.all()
        serializer = class_serializers.ClassSerializer(classes, many=True)
        return Response(serializer.data)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = account_models.Teacher.objects.all()
    serializer_class = account_serializers.TeacherSerializer

    @list_route(['get'], authentication_classes=[TokenAuthentication],
                permission_classes=[IsAuthenticated], url_path="get-classes")
    def get_classes(self, request):
        teacher = account_models.Teacher.objects.get(user=request.user)
        classes = teacher.class_set.all()
        serializer = class_serializers.ClassSerializer(classes, many=True)
        return Response(serializer.data)
