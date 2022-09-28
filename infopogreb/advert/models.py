from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from autoslug import AutoSlugField 
from uuslug import uuslug



# def gen_slug(s):
#     new_slug = slugify(s, allow_unicode=True)
#     return new_slug + '-' + str(int(time()))

def instance_slug(instance):
    return instance.subject

def slugify_value(value):
    return value.replace(' ', '-')

class Category(models.Model):
    """Категории объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = AutoSlugField('URL', max_length=100, db_index=True, unique=True, populate_from=instance_slug, slugify=slugify_value)
    icon = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
         return self.name
     
    def save(self, *args, **kwargs):
        self.slug = uuslug(self.slug, instance=self)
        super(Advert, self).save(*args, **kwargs)
     
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
    
    category = models.ForeignKey(Category, verbose_name="Категорія*", on_delete=models.CASCADE)
    types_ad = models.CharField(max_length=9, choices=TYPE_AD, blank=True, verbose_name="тип об'яви")
    types_pr = models.CharField(max_length=9, choices=TYPE_PRODUCT, blank=True, verbose_name='стан товару')
    subject = models.CharField("Назва*", max_length=200)
    description = models.TextField("Опис об'яви*", max_length=10000)
    images = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True)
    price = models.IntegerField("ціна", default=0, blank=True, null=True)
    name = models.CharField("Ваше ім'я*", max_length=50)
    email = models.EmailField(blank=True, verbose_name='эл.почта')
    telefon = models.CharField('номер телефона', blank=True, max_length=13)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    moderation = models.BooleanField("Модерация", default=True)
    slug = AutoSlugField('URL', max_length=100, db_index=True, unique=True, populate_from=instance_slug, slugify=slugify_value)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    location = models.CharField('Локація', max_length=50, blank=True)
    

    
    def save(self, *args, **kwargs):
        self.slug = uuslug(self.slug, instance=self)
        super(Advert, self).save(*args, **kwargs)
            

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("detail_advert", kwargs={ "slug": self.slug})

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"