# Generated by Django 4.1.6 on 2023-05-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_candidatos_diaria_candidatas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaria',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='diaria',
            name='valor_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
