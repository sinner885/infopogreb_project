# Generated by Django 4.0.5 on 2022-08-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_alter_advert_category_alter_advert_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True, verbose_name='url'),
        ),
    ]
