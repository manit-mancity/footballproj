from django.db import models

# Create your models here.

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goals = models.IntegerField()
    assists = models.IntegerField()
    matches_played = models.IntegerField()

    def __str__(self):
        return self.name