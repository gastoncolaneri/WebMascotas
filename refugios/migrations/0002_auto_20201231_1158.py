# Generated by Django 3.0.4 on 2020-12-31 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refugios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refugio',
            old_name='email_again',
            new_name='confirmacionEmail',
        ),
    ]
