from django.db import models


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
    description_long = models.TextField(
        verbose_name='Полное описание',
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
    place = models.ForeignKey(
        Places,
        verbose_name='Place',
        # related_name='images',
        on_delete=models.DO_NOTHING,
        )
    img = models.ImageField(
        verbose_name='Фото',
        )

    def __str__(self):
        return f'{self.pk} {self.place}'
