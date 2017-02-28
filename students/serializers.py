from rest_framework import serializers
from rest_framework.authtoken.models import Token

from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def validate(self, attrs):
        token = Token.objects.get(pk=self.context.get('token_id'))
        attrs['user'] = token.user
        return attrs
