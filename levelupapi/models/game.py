from django.db import models
from levelupapi.models.gamer import Gamer
from levelupapi.models.game_type import GameType

class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=12)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
