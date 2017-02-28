from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from accounts.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def get_serializer_context(self):
        return {'token_id', Token.objects.get(user=self.request.user).pk}
