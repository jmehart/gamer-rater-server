# Generated by Django 4.0.4 on 2022-05-10 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raterapp', '0008_rename_gameid_image_game_rename_gamerid_image_gamer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamecategory',
            old_name='categoryId',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='gamecategory',
            old_name='gameId',
            new_name='game',
        ),
    ]
