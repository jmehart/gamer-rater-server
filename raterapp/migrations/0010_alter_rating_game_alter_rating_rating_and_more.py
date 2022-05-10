# Generated by Django 4.0.4 on 2022-05-10 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raterapp', '0009_rename_categoryid_gamecategory_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='raterapp.game'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='raterapp.game'),
        ),
    ]
