# Generated by Django 4.0.5 on 2022-09-26 19:47

import autoslug.fields
from django.db import migrations
import service.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryservice',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from=service.models.instance_slug, slugify=service.models.slugify_value, unique=True, verbose_name='URL'),
        ),
    ]
