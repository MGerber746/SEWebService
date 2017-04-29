from rest_framework import serializers

from accounts.models import Student
from grades.models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        if Student.objects.filter(user=user):
            attrs['student'] = Student.objects.get(user=user)
        else:
            raise serializers.ValidationError("Must be a student to post a grade")
        return attrs
