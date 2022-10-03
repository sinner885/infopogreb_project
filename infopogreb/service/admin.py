from django.contrib import admin
from django import forms
from .models import CategoryService, Service
from ckeditor_uploader.widgets import CKEditorUploadingWidget

@admin.register(CategoryService)
class CategoryServiceAdmin(admin.ModelAdmin):
    """Категории услуг"""
    list_display = ("name", "id", 'icon')
    prepopulated_fields = {"slug": ("name",)}
    
class ServiceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Service
        fields = '__all__'

   
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Послуги"""
    form = ServiceAdminForm
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