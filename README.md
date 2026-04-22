# Pinnacle Football Analytics

A Django web app for tracking and comparing UEFA Champions League teams and players. Select the teams and players you want to follow, view individual player stats, and run head-to-head comparisons with detailed attacking, defensive, and discipline data.

---

## Features

- **Dashboard** — pick teams and players to track from all 36 UCL 2024/25 clubs
- **Player detail pages** — goals, assists, per-game averages, ratings, and performance bars
- **Compare** — side-by-side comparison for teams (match record, goals, defence, possession, discipline) and players (attacking, defensive, creative, and discipline stats)
- **Ratings system** — automatic player rating out of 10 based on goals, assists, and contributions per game

---

## Tech Stack

- Python 3.13
- Django 6.0.2
- SQLite (default, no setup required)
- Vanilla HTML/CSS/JS (no frontend framework)

---

## Getting Started

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd pinnacle4football
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Seed the database with team data

```bash
python manage.py seed_ucl_teams
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
pinnacle4football/
├── backend/                    # Main app
│   ├── management/
│   │   └── commands/
│   │       ├── seed_ucl_teams.py   # Seeds all 36 UCL teams with stats
│   │       └── reset_db.py         # Clears the database
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   │   ├── dashboard.html
│   │   ├── compare.html
│   │   ├── player.html
│   │   └── player_detail.html
│   ├── models.py               # Team, Player, TrackedTeam models
│   ├── views.py                # All view logic
│   ├── urls.py                 # App URL patterns
│   └── forms.py                # Team and Player forms
├── config/                     # Django project config
│   ├── settings.py
│   └── urls.py
├── data/
│   └── sample players.csv      # Player data loaded by the app
└── manage.py
```

---

## Player Data

Players are loaded from `data/sample players.csv`. The CSV supports the following columns:

| Column | Description |
|---|---|
| `name` | Player name |
| `team` | Club name |
| `goals` | Season goals |
| `assists` | Season assists |
| `matches_played` | Appearances |
| `tackles` | Total tackles |
| `interceptions` | Total interceptions |
| `key_passes` | Total key passes |
| `dribbles` | Successful dribbles |
| `yellow_cards` | Yellow cards received |
| `red_cards` | Red cards received |

To update player data, edit the CSV and restart the server — no migration needed.

---

## Management Commands

Reset the database:
```bash
python manage.py reset_db
```

Re-seed teams (safe to run multiple times — uses update_or_create):
```bash
python manage.py seed_ucl_teams
```

---

## Notes

- `DEBUG = True` and the `SECRET_KEY` in `settings.py` are fine for local development but must be changed before any kind of deployment
- The database file (`db.sqlite3`) is excluded from version control — each developer runs migrations and the seed command locally
- Player ratings are calculated dynamically in `views.py`, not stored in the database