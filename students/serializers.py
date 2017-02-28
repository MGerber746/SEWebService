from rest_framework import serializers
from rest_framework.authtoken.models import Token

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        token = Token.objects.get(pk=self.context.get('token_id'))
        attrs['user'] = token.user
        return attrs
