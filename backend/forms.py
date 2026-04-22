from django import forms
from .models import Team, Player


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name', 'league', 'country',
            'matches_played', 'wins', 'draws', 'losses',
            'goals_scored', 'goals_conceded',
        ]
        widgets = {
            'name':           forms.TextInput(attrs={'placeholder': 'e.g. Manchester City'}),
            'league':         forms.TextInput(attrs={'placeholder': 'e.g. Premier League'}),
            'country':        forms.TextInput(attrs={'placeholder': 'e.g. England'}),
            'matches_played': forms.NumberInput(attrs={'min': 0}),
            'wins':           forms.NumberInput(attrs={'min': 0}),
            'draws':          forms.NumberInput(attrs={'min': 0}),
            'losses':         forms.NumberInput(attrs={'min': 0}),
            'goals_scored':   forms.NumberInput(attrs={'min': 0}),
            'goals_conceded': forms.NumberInput(attrs={'min': 0}),
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team', 'goals', 'assists', 'matches_played']
        widgets = {
            'name':           forms.TextInput(attrs={'placeholder': 'e.g. Erling Haaland'}),
            'goals':          forms.NumberInput(attrs={'min': 0}),
            'assists':        forms.NumberInput(attrs={'min': 0}),
            'matches_played': forms.NumberInput(attrs={'min': 0}),
        }