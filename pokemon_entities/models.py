from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(auto_now_add=True)
    disappeared_at = models.DateTimeField(null=True)
    level = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    protection = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
