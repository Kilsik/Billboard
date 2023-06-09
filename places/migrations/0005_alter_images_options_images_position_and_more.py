# Generated by Django 4.2.2 on 2023-06-09 17:32

from django.db import migrations, models
import django.db.models.deletion


def fill_positions(apps, schema_editor):
    Images = apps.get_model('places', 'Images')
    for image in Images.objects.all():
        image.position = image.pk
        image.save()


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_places_short_title_alter_places_placeid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии'
                },
        ),
        migrations.AddField(
            model_name='images',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='images',
            name='place',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='places.places',
                verbose_name='Place'
                ),
        ),
        migrations.RunPython(fill_positions),
    ]