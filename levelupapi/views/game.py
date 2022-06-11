"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game
from levelupapi.models.game_type import GameType
from levelupapi.models.gamer import Gamer


class GameView(ViewSet):
    """Level up Game view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Game"""  

        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all Games """
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games """
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'title', 'maker', 'gamer', 'number_of_players', 'skill_level')
        

def create(self, request):
    """Handle POST operations

    Returns
        Response -- JSON serialized game instance
    """
    gamer = Gamer.objects.get(user=request.auth.user)
    game_type = GameType.objects.get(pk=request.data["game_type"])

    game = Game.objects.create(
        title=request.data["title"],
        maker=request.data["maker"],
        number_of_players=request.data["number_of_players"],
        skill_level=request.data["skill_level"],
        gamer=gamer,
        game_type=game_type
    )
    serializer = GameSerializer(game)
    return Response(serializer.data)