# Generated by Django 5.1.3 on 2024-11-30 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("news", "0001_initial"),
        ("schedule", "0001_initial"),
        ("wagtailimages", "0027_image_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="newspage",
            name="game_is",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="game_description",
                to="schedule.result",
            ),
        ),
        migrations.AddField(
            model_name="newspage",
            name="intro_image",
            field=models.ForeignKey(
                help_text="News intro image",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
