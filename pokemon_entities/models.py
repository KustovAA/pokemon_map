from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, default='', blank=True, verbose_name='Название на английском')
    title_jp = models.CharField(max_length=200, default='', blank=True, verbose_name='Название на японском')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    description = models.TextField(default='', blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        to='pokemon_entities.Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pokemon_previous_evolution',
        verbose_name='Из кого эволюционирует'
    )
    next_evolution = models.ForeignKey(
        to='pokemon_entities.Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pokemon_next_evolution',
        verbose_name='В кого эволюционирует'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon', verbose_name='Покемон')
    appeared_at = models.DateTimeField(verbose_name='Время появления')
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения')
    level = models.IntegerField(default=0, verbose_name='Уровень')
    health = models.IntegerField(default=0, verbose_name='Здоровье')
    damage = models.IntegerField(default=0, verbose_name='Урон')
    protection = models.IntegerField(default=0, verbose_name='Защита')
    stamina = models.IntegerField(default=0, verbose_name='Выносливость')

    def __str__(self):
        return f'Entity {self.id} for {self.pokemon.title}'
