# Generated by Django 5.1.3 on 2024-11-30 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_date", models.DateTimeField()),
                (
                    "game_type",
                    models.CharField(
                        choices=[
                            ("PIRMA LYGA", "TOP SPORT PIRMA LYGA"),
                            ("DRAUGISKOS", "DRAUGIŠKOS RUNGTYNĖS"),
                            ("LFF TAURE", "LFF TAURĖ"),
                        ],
                        default="PIRMA LYGA",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "ordering": ["game_date"],
            },
        ),
        migrations.CreateModel(
            name="SchedulePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("home_team_score", models.CharField(max_length=2)),
                ("away_team_score", models.CharField(max_length=2)),
                (
                    "the_game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="game_result",
                        to="schedule.game",
                    ),
                ),
            ],
            options={
                "ordering": ["-the_game__game_date"],
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                (
                    "logo",
                    models.ForeignKey(
                        help_text="Team logo",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="game",
            name="away_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="schedule.team",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="home_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="schedule.team",
            ),
        ),
    ]
