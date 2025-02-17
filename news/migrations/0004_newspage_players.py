# Generated by Django 5.1.4 on 2024-12-08 15:40

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_newspage_game_is"),
    ]

    operations = [
        migrations.AddField(
            model_name="newspage",
            name="players",
            field=wagtail.fields.StreamField(
                [("player", 0)],
                blank=True,
                block_lookup={
                    0: (
                        "wagtail.snippets.blocks.SnippetChooserBlock",
                        ("team.ClubMember",),
                        {"required": False},
                    )
                },
            ),
        ),
    ]
