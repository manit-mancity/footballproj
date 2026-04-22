from django.core.management.base import BaseCommand
from backend.models import Team, Player


class Command(BaseCommand):
    help = 'Clears all teams and players so you can start fresh (no pre-seeded data).'

    def handle(self, *args, **options):
        p_count = Player.objects.count()
        t_count = Team.objects.count()
        Player.objects.all().delete()
        Team.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(
            f'Deleted {p_count} player(s) and {t_count} team(s). Database is now empty.'
        ))