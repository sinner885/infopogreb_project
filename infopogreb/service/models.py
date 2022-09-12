from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class CategoryService(models.Model):
    """Категории услуг"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)
    icon = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
         return self.name
     
    class Meta:
         verbose_name = "Категория услуг"
         verbose_name_plural ='Категории услуг'



class Service(models.Model):
    """Послуги"""
    category = models.ForeignKey(CategoryService, verbose_name="Категорія", on_delete=models.CASCADE)
    subject = models.CharField("Назва послуги", max_length=200)
    description = models.TextField("Опис посуги", max_length=10000)
    images = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, blank=True)
    location = models.CharField('Адреса', max_length=20)
    name = models.CharField("Ваше ім'я", max_length=50)
    email = models.EmailField(blank=True, verbose_name='эл.почта')
    telefon = models.CharField('номер телефона', blank=True, max_length=13)
    moderation = models.BooleanField("Модерация", default=True)
    slug = models.SlugField("url", max_length=200, unique=True, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    views = models.IntegerField('количество просмотров', default=0)
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.subject)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"