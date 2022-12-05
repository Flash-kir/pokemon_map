from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None
        )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None
        )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None
        )
    next_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='evolution_next'
        )
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='evolution_previous'
        )
    description = models.TextField(null=True, blank=True, default=None)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, default=None)
    disappeared_at = models.DateTimeField(null=True, default=None)
    level = models.FloatField(blank=True, null=True, default=None)
    health = models.FloatField(blank=True, null=True, default=None)
    strength = models.FloatField(blank=True, null=True, default=None)
    defence = models.FloatField(blank=True, null=True, default=None)
    stamina = models.FloatField(blank=True, null=True, default=None)
