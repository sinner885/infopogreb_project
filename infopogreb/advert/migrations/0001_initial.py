# Generated by Django 4.0.5 on 2022-07-19 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('icon', models.ImageField(blank=True, upload_to='photos/%Y/%m/%D/')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_ad', models.CharField(choices=[('k', 'куплю'), ('p', 'продам'), ('o', 'обменяю')], max_length=1, verbose_name='тип объявления')),
                ('types_pr', models.CharField(choices=[('a', 'новое'), ('b', 'б/у')], max_length=1, verbose_name='состояние товара')),
                ('subject', models.CharField(max_length=200, verbose_name='Назва')),
                ('description', models.TextField(max_length=10000, verbose_name='Опис обяви')),
                ('images', models.ImageField(blank=True, upload_to='photos/%Y/%m/%D')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ціна')),
                ('name', models.CharField(help_text='Ваше имя', max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, help_text='электронна почта', max_length=254, verbose_name='эл.почта')),
                ('telefon', models.CharField(blank=True, max_length=13, verbose_name='номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('category', models.ForeignKey(help_text='выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='advert.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
