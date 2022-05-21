from django.db import models
from levelupapi.models.game import Game
from levelupapi.models.gamer import Gamer

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.DateTimeField()
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
