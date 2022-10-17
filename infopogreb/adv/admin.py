from django.contrib import admin
from .models import Adv

@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    '''Оголошення'''
    list_display = ('name', 'description', 'created', 'user', 'moderation', 'contact')