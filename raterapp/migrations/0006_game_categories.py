# Generated by Django 4.0.4 on 2022-05-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raterapp', '0005_remove_game_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(related_name='games', through='raterapp.GameCategory', to='raterapp.category'),
        ),
    ]
