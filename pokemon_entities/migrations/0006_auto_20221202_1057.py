# Generated by Django 3.1.14 on 2022-12-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20221202_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.FloatField(default=None, null=True),
        ),
    ]
