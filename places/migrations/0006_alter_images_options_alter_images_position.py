# Generated by Django 4.2.2 on 2023-06-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_images_options_images_position_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['position'], 'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='images',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
