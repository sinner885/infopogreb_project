# Generated by Django 4.0.5 on 2022-09-26 19:47

import advert.models
import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0008_alter_advert_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from=advert.models.instance_slug, slugify=advert.models.slugify_value, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from=advert.models.instance_slug, slugify=advert.models.slugify_value, unique=True, verbose_name='URL'),
        ),
    ]