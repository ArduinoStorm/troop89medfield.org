# Generated by Django 2.1 on 2019-03-01 01:29

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
