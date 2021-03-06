# Generated by Django 4.0.4 on 2022-05-06 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('designer', models.CharField(max_length=55)),
                ('year_released', models.IntegerField()),
                ('num_of_players', models.IntegerField()),
                ('estimated_time', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=55)),
                ('gameId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.game')),
                ('gamerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=55)),
                ('gameId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.game')),
                ('gamerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=55)),
                ('gameId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.game')),
                ('gamerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.category')),
                ('gameId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='gamerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterapp.gamer'),
        ),
    ]
