# Generated by Django 4.1.6 on 2023-05-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_diaria_data_atendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='complemento',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
