# Generated by Django 4.1.1 on 2022-09-30 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]