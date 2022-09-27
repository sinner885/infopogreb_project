from django.contrib import admin
from .models import CategoryService, Service

@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    """Категории услуг"""
    list_display = ("name", "id", 'icon')
    #prepopulated_fields = {"slug": ("name",)}
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Послуги"""
    list_display = (
        "id",
        "brend",
        "subject",
        "slug",
        "user",
        "category",
        'name',
        'email',
        "moderation",
        'telefon',
        'location',
        'created',
        'views'
    )
    list_display_links = ("subject",)
    
    #prepopulated_fields = {"slug": ("user", "subject")}