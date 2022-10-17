from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

class Adv(models.Model):
    '''Оголошення'''
    name = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис', max_length=400)
    photo = models.ImageField("Фото", upload_to='photos/%Y/%m/%d/', blank=True, height_field=None, width_field=None)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    moderation = models.BooleanField("Модерация", default=True)
    contact = models.CharField('Контакти', max_length=50, blank=True)
    
    def get_absolute_url(self):
        return reverse("detail_adv", kwargs={"pk": self.pk})
    
    
    
    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"
        
