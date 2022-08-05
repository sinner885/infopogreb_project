from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Категории объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)
    icon = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
         return self.name
     
    class Meta:
         verbose_name = "Категория"
         verbose_name_plural ='Категории'



class Advert(models.Model):
    """Объявления"""
    TYPE_PRODUCT = (
        ('нове', 'нове'),
        ('подержане', 'подержане'),
    )
    TYPE_AD = (
        ('куплю', 'куплю'),
        ('продам', 'продам'),
        ('обміняю', 'обміняю'),
        ('віддам', 'віддам'),
        ('аренда', 'аренда')
    )
    
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.CASCADE)
    types_ad = models.CharField(max_length=9, choices=TYPE_AD, blank=True, verbose_name="тип об'яви")
    types_pr = models.CharField(max_length=9, choices=TYPE_PRODUCT, blank=True, verbose_name='стан товару')
    subject = models.CharField("Назва", max_length=200)
    description = models.TextField("Опис об'яви", max_length=10000)
    images = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    price = models.DecimalField("ціна", max_digits=8, decimal_places=2,blank=True, null=True)
    name = models.CharField('Имя', max_length=50, help_text='Ваше имя')
    email = models.EmailField(blank=True, verbose_name='эл.почта')
    telefon = models.CharField('номер телефона', blank=True, max_length=13)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    moderation = models.BooleanField("Модерация", default=True)
    slug = models.SlugField("url", max_length=200, unique=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    location = models.CharField('Локація', max_length=20)
    

    

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("detail_advert", kwargs={ "slug": self.slug})

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"