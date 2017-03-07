from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from games.models import Game
from games.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAdminUser,)
