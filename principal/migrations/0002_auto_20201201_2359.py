# Generated by Django 3.0.4 on 2020-12-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='codigoArea',
            field=models.IntegerField(verbose_name='Código de área'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='confirmacionEmail',
            field=models.EmailField(max_length=254, verbose_name='Confirmación Email'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='cp',
            field=models.CharField(max_length=40, verbose_name='Código Postal'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(verbose_name='Teléfono'),
        ),
    ]
