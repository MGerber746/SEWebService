from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts import models as account_models


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(allow_blank=False, style={'input_type': 'password'})
    confirm_password = serializers.CharField(allow_blank=False,
                                             style={'input_type': 'password'},
                                             write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password', 'confirm_password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'user_permissions', 'last_login', 'groups')

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        # After saving the user, create a token for that user.
        Token.objects.create(user=user)
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.Student
        fields = '__all__'

    def validate(self, attrs):
        token = Token.objects.get(pk=self.context.get('token_id'))
        attrs['user'] = token.user
        return attrs


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.Teacher
        fields = '__all__'

    def validate(self, attrs):
        token = Token.objects.get(pk=self.context.get('token_id'))
        attrs['user'] = token.user
        if account_models.Teacher.objects.filter(pk=attrs['user'].pk) == 0:
            raise serializers.ValidationError("You must be a teacher to access this endpoint")
        return attrs
