# Generated by Django 4.0.5 on 2022-09-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_service_options_service_created_service_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='brend',
            field=models.CharField(blank=True, max_length=50, verbose_name='Назва бренду'),
        ),
    ]