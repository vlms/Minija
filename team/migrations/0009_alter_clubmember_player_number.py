# Generated by Django 5.1.4 on 2024-12-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0008_alter_teampage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clubmember",
            name="player_number",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
