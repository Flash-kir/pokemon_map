from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Имя на русском',
        )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Имя на английском',
        )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Имя на японском',
        )
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name='Эволюционирует из',
        )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Изображение',
        )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.SET_NULL,
        null=True,
        related_name='entities',
        verbose_name='Покемон',
        )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        null=True,
        verbose_name='Время появления',
        )
    disappeared_at = models.DateTimeField(
        null=True,
        verbose_name='Время исчезновения',
        )
    level = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Уровень'
        )
    health = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Здоровье'
        )
    strength = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Сила'
        )
    defence = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Защита'
        )
    stamina = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Выносливость'
        )
