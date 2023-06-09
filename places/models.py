from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Наименование',
        )
    short_title = models.CharField(
        max_length=50,
        verbose_name='Краткое наименование',
        blank=True,
        null=True,
        )
    placeid = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='PlaceId',
        )
    description_short = models.CharField(
        max_length=500,
        verbose_name='Краткое описание',
        )
    description_long = HTMLField(
        verbose_name='Полное описание'
        )
    lng = models.FloatField(
        verbose_name='Долгота',
        )
    lat = models.FloatField(
        verbose_name='Широта'
        )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'


class Images(models.Model):
    position = models.PositiveIntegerField(
        verbose_name='Позиция',
        default=0,
        )
    place = models.ForeignKey(
        Places,
        verbose_name='Place',
        on_delete=models.DO_NOTHING,
        )
    img = models.ImageField(
        verbose_name='Фото',
        )

    def __str__(self):
        return f'{self.pk} {self.place}'

    def preview(self):
        height = 200
        width = self.img.width*height/self.img.height
        return mark_safe(
            f'<img src={ self.img.url } width={width} height={height}>'
            )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['position', ]
