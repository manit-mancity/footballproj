from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_player_pinned_team_pinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='clean_sheets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='yellow_cards',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='red_cards',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='shots_on_target',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='possession',
            field=models.FloatField(default=0.0),
        ),
    ]