# Generated by Django 3.0.4 on 2021-05-01 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugios', '0002_auto_20210501_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refugio',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico'),
        ),
    ]