# Generated by Django 4.1.6 on 2023-05-19 00:58

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_usuario_is_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]