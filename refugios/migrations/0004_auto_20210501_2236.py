# Generated by Django 3.0.4 on 2021-05-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugios', '0003_auto_20210501_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refugio',
            name='celular',
            field=models.IntegerField(blank=True, null=True, verbose_name='Celular'),
        ),
    ]
