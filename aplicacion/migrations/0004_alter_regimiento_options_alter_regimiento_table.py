# Generated by Django 4.2.2 on 2023-08-28 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_fuerza_options_alter_pais_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regimiento',
            options={'verbose_name': 'unidad', 'verbose_name_plural': 'unidades'},
        ),
        migrations.AlterModelTable(
            name='regimiento',
            table='unidad',
        ),
    ]
