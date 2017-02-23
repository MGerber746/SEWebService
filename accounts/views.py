from rest_framework import viewsets

from accounts import serializers
from accounts.models import UserAccount


class AccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = serializers.AccountSerializer
