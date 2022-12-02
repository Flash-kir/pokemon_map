from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, default=None)
    disappeared_at = models.DateTimeField(null=True, default=None)
    level = models.FloatField(null=True, default=None)
    health = models.FloatField(null=True, default=None)
    strength = models.FloatField(null=True, default=None)
    defence = models.FloatField(null=True, default=None)
    stamina = models.FloatField(null=True, default=None)
