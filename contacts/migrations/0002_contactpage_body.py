# Generated by Django 5.0.10 on 2024-12-05 18:57

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactpage",
            name="body",
            field=wagtail.fields.RichTextField(null=True),
        ),
    ]
