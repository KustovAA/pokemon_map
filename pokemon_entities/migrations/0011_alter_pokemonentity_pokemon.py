# Generated by Django 4.1.1 on 2022-10-07 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_alter_pokemon_description_alter_pokemon_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
