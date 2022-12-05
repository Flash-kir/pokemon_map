from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Имя на русском',
        )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Имя на английском',
        )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default=None,
        verbose_name='Имя на японском',
        )
    next_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='evolution_next',
        verbose_name='Эволюционирует в',
        )
    previous_evolution = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='evolution_previous',
        verbose_name='Эволюционирует из',
        )
    description = models.TextField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Описание',
        )
    image = models.ImageField(
        upload_to='media',
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
        verbose_name='Покемон',
        )
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    appeared_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='Время появления',
        )
    disappeared_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='Время исчезновения',
        )
    level = models.FloatField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Уровень'
        )
    health = models.FloatField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Здоровье'
        )
    strength = models.FloatField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Сила'
        )
    defence = models.FloatField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Защита'
        )
    stamina = models.FloatField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Выносливость'
        )
