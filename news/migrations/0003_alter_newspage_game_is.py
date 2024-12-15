# Generated by Django 5.1.3 on 2024-12-03 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_initial"),
        ("schedule", "0002_alter_result_the_game"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspage",
            name="game_is",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="schedule.result",
            ),
        ),
    ]
