from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, null=True, blank=True)
    title_jp = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    previous_evolution = models.ForeignKey(
        'pokemon_entities.Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pokemon_entities_Pokemon_previous_evolution'
    )
    next_evolution = models.ForeignKey(
        'pokemon_entities.Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pokemon_entities_Pokemon_next_evolution'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    protection = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)

    def __str__(self):
        return f'Entity {self.id} for {self.pokemon.title}'
