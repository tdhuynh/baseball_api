# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseball_api_app', '0002_batting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_code', models.IntegerField(null=True)),
                ('stint', models.IntegerField(null=True)),
                ('team_code', models.CharField(blank=True, max_length=10)),
                ('league_code', models.CharField(blank=True, max_length=10)),
                ('wins', models.IntegerField(null=True)),
                ('losses', models.IntegerField(null=True)),
                ('games', models.IntegerField(null=True)),
                ('games_started', models.IntegerField(null=True)),
                ('completed_games', models.IntegerField(null=True)),
                ('shutouts', models.IntegerField(null=True)),
                ('saves', models.IntegerField(null=True)),
                ('outs_pitched', models.IntegerField(null=True)),
                ('hits', models.IntegerField(null=True)),
                ('earned_runs', models.IntegerField(null=True)),
                ('homeruns', models.IntegerField(null=True)),
                ('walks', models.IntegerField(null=True)),
                ('strikeouts', models.IntegerField(null=True)),
                ('opponent_batting_average', models.IntegerField(null=True)),
                ('earned_run_average', models.IntegerField(null=True)),
                ('intentional_walks', models.IntegerField(null=True)),
                ('wild_pitches', models.IntegerField(null=True)),
                ('batters_hit_by_pitch', models.IntegerField(null=True)),
                ('balks', models.IntegerField(null=True)),
                ('batters_faced_by_pitcher', models.IntegerField(null=True)),
                ('games_finished', models.IntegerField(null=True)),
                ('runs_allowed', models.IntegerField(null=True)),
                ('sacrifices_by_opp_batters', models.IntegerField(null=True)),
                ('sacrifice_flies_by_opp_batters', models.IntegerField(null=True)),
                ('grounded_into_double_plays_by_opp_batters', models.IntegerField(null=True)),
                ('player_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseball_api_app.Master')),
            ],
        ),
        migrations.RenameField(
            model_name='batting',
            old_name='base_on_balls',
            new_name='walks',
        ),
    ]