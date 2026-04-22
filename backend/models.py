from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    clean_sheets = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    shots_on_target = models.IntegerField(default=0)
    possession = models.FloatField(default=0.0)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TrackedTeam(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    league = models.CharField(max_length=100, default='UEFA Champions League')

    class Meta:
        unique_together = ('name', 'league')

    def __str__(self):
        return self.name