# Generated by Django 2.1 on 2018-08-03 23:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('trooporg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrol',
            name='date_retired',
        ),
    ]
