from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Team, Player

from django.shortcuts import render

def dashboard(request):
    teams = Team.objects.all()
    players = Player.objects.all()

    return render(request, 'dashboard.html', {
        'teams': teams,
        'players': players
    })