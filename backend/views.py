import csv
import os
from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Value, IntegerField
from django.db.models.functions import Coalesce
from .models import Team

UCL_TEAMS = [
    {"name": "Manchester City",     "country": "England",        "league": "Premier League"},
    {"name": "Liverpool",           "country": "England",        "league": "Premier League"},
    {"name": "Arsenal",             "country": "England",        "league": "Premier League"},
    {"name": "Chelsea",             "country": "England",        "league": "Premier League"},
    {"name": "Aston Villa",         "country": "England",        "league": "Premier League"},
    {"name": "Real Madrid",         "country": "Spain",          "league": "La Liga"},
    {"name": "Barcelona",           "country": "Spain",          "league": "La Liga"},
    {"name": "Atlético Madrid",     "country": "Spain",          "league": "La Liga"},
    {"name": "Girona",              "country": "Spain",          "league": "La Liga"},
    {"name": "Bayern Munich",       "country": "Germany",        "league": "Bundesliga"},
    {"name": "Borussia Dortmund",   "country": "Germany",        "league": "Bundesliga"},
    {"name": "RB Leipzig",          "country": "Germany",        "league": "Bundesliga"},
    {"name": "Bayer Leverkusen",    "country": "Germany",        "league": "Bundesliga"},
    {"name": "Stuttgart",           "country": "Germany",        "league": "Bundesliga"},
    {"name": "Paris Saint-Germain", "country": "France",         "league": "Ligue 1"},
    {"name": "Brest",               "country": "France",         "league": "Ligue 1"},
    {"name": "Monaco",              "country": "France",         "league": "Ligue 1"},
    {"name": "Lille",               "country": "France",         "league": "Ligue 1"},
    {"name": "Inter Milan",         "country": "Italy",          "league": "Serie A"},
    {"name": "AC Milan",            "country": "Italy",          "league": "Serie A"},
    {"name": "Juventus",            "country": "Italy",          "league": "Serie A"},
    {"name": "Atalanta",            "country": "Italy",          "league": "Serie A"},
    {"name": "Bologna",             "country": "Italy",          "league": "Serie A"},
    {"name": "Benfica",             "country": "Portugal",       "league": "Primeira Liga"},
    {"name": "Porto",               "country": "Portugal",       "league": "Primeira Liga"},
    {"name": "Sporting CP",         "country": "Portugal",       "league": "Primeira Liga"},
    {"name": "PSV Eindhoven",       "country": "Netherlands",    "league": "Eredivisie"},
    {"name": "Feyenoord",           "country": "Netherlands",    "league": "Eredivisie"},
    {"name": "Club Brugge",         "country": "Belgium",        "league": "Pro League"},
    {"name": "Celtic",              "country": "Scotland",       "league": "Scottish Premiership"},
    {"name": "Shakhtar Donetsk",    "country": "Ukraine",        "league": "Ukrainian Premier League"},
    {"name": "Red Star Belgrade",   "country": "Serbia",         "league": "Serbian SuperLiga"},
    {"name": "Dinamo Zagreb",       "country": "Croatia",        "league": "HNL"},
    {"name": "Salzburg",            "country": "Austria",        "league": "Austrian Bundesliga"},
    {"name": "Sturm Graz",          "country": "Austria",        "league": "Austrian Bundesliga"},
    {"name": "Slavia Prague",       "country": "Czech Republic", "league": "Czech First League"},
]


def _load_csv_players():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSV_PATH = os.path.join(BASE_DIR, 'data', 'sample players.csv')
    players = []
    try:
        with open(CSV_PATH, newline='', encoding='utf-8') as f:
            for i, row in enumerate(csv.DictReader(f)):
                goals         = int(row.get('goals', 0))
                assists       = int(row.get('assists', 0))
                matches       = int(row.get('matches_played', 0))
                tackles       = int(row.get('tackles', 0))
                interceptions = int(row.get('interceptions', 0))
                key_passes    = int(row.get('key_passes', 0))
                dribbles      = int(row.get('dribbles', 0))
                yellow_cards  = int(row.get('yellow_cards', 0))
                red_cards     = int(row.get('red_cards', 0))

                m   = matches if matches > 0 else 1
                gpg = round(goals / m, 2)
                apg = round(assists / m, 2)
                gc  = goals + assists
                tpg = round(tackles / m, 2)
                ipg = round(interceptions / m, 2)
                kpg = round(key_passes / m, 2)
                dpg = round(dribbles / m, 2)

                raw    = (gpg * 4) + (apg * 3) + (round(gc / m, 2) * 3)
                rating = min(round(raw, 1), 10.0)
                rc     = 'excellent' if rating >= 7 else 'good' if rating >= 5 else 'average' if rating >= 3 else 'poor'

                players.append({
                    'id':            i,
                    'name':          row.get('name', '').strip(),
                    'team':          row.get('team', '').strip(),
                    'goals':         goals,
                    'assists':       assists,
                    'matches_played': matches,
                    'gc':            gc,
                    'gpg':           gpg,
                    'apg':           apg,
                    'rating':        rating,
                    'rc':            rc,
                    'tackles':       tackles,
                    'interceptions': interceptions,
                    'key_passes':    key_passes,
                    'dribbles':      dribbles,
                    'yellow_cards':  yellow_cards,
                    'red_cards':     red_cards,
                    'tpg':           tpg,
                    'ipg':           ipg,
                    'kpg':           kpg,
                    'dpg':           dpg,
                })
    except FileNotFoundError:
        pass
    return players


def dashboard(request):
    all_players = _load_csv_players()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'set_teams':
            request.session['selected_teams'] = request.POST.getlist('teams')
            request.session.modified = True
        elif action == 'set_players':
            request.session['selected_players'] = [int(p) for p in request.POST.getlist('players')]
            request.session.modified = True
        return redirect('dashboard')

    selected_team_names = request.session.get('selected_teams', [])
    selected_player_ids = request.session.get('selected_players', [])

    context = {
        'all_teams':           UCL_TEAMS,
        'all_players':         all_players,
        'selected_teams':      [t for t in UCL_TEAMS if t['name'] in selected_team_names],
        'selected_players':    [p for p in all_players if p['id'] in selected_player_ids],
        'selected_team_names': set(selected_team_names),
        'selected_player_ids': set(selected_player_ids),
    }
    return render(request, 'dashboard.html', context)


def player_detail(request, player_id):
    players = _load_csv_players()
    try:
        player = players[int(player_id)]
    except (IndexError, ValueError):
        return redirect('dashboard')
    return render(request, 'player.html', {'player': player})


def compare(request):
    teams = Team.objects.annotate(
        player_count=Count('player'),
        squad_goals=Coalesce(Sum('player__goals'), Value(0), output_field=IntegerField()),
        squad_assists=Coalesce(Sum('player__assists'), Value(0), output_field=IntegerField()),
    )
    return render(request, 'compare.html', {
        'all_teams':   teams,
        'all_players': _load_csv_players(),
    })