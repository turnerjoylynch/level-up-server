"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer


class EventView(ViewSet):
    """Level up events view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event"""  

        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all events """
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')
        
        
def create(self, request):
    """Handle POST operations

    Returns
        Response -- JSON serialized game instance
    """
    game = Game.objects.get(user=request.auth.user)
    gamer = Gamer.objects.get(user=request.auth.user)

    event = Event.objects.create(
        game=game,
        description=request.data["description"],
        date=request.data["date"],
        time=request.data["time"],
        organizer=gamer,
    )
    serializer = EventSerializer(event)
    return Response(serializer.data)