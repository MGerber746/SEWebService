from rest_framework import serializers
from rest_framework.authtoken.models import Token

from classes.models import Class
from teachers.models import Teacher


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

    def validate(self, attrs):
        token = Token.objects.get(pk=self.context.get('token_id'))
        attrs['teacher'] = Teacher.objects.get(user=token.user)
        return attrs
