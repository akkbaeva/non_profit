# Generated by Django 3.2.3 on 2021-05-21 14:17

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('npo_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='npouser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
