from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование',
    )
    description_short = models.TextField(
        verbose_name='Краткое описание',
        blank=True,
    )
    description_long = HTMLField(
        verbose_name='Полное описание',
        blank=True,
    )
    lng = models.FloatField(
        verbose_name='Долгота',
    )
    lat = models.FloatField(
        verbose_name='Широта'
    )

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return f'{self.title}'


class Images(models.Model):
    position = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
    )
    place = models.ForeignKey(
        Places,
        verbose_name='Place',
        on_delete=models.DO_NOTHING,
        related_name='images'
    )
    img = models.ImageField(
        verbose_name='Фото',
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['position', ]

    def __str__(self):
        return f'{self.pk} {self.place}'
