from django import forms

from .models import Service

class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ('category', 'brend', 'subject', 'description', 'images', 'name', 'telefon', 'email', 'location')
        widgets = {
            'category': forms.Select(attrs={'class': 'single-input'}),
            'brend': forms.TextInput(attrs={'class': 'single-input'}),
            'subject': forms.TextInput(attrs={'class': 'single-input'}),
            'slug': forms.TextInput(attrs={'class': 'single-input'}),
            'description': forms.Textarea(attrs={'class': 'single-input', 'rows':6}),
            'images': forms.ClearableFileInput(attrs={'class': 'single-input'}),
            'name': forms.TextInput(attrs={'class': 'single-input'}),
            'telefon': forms.TextInput(attrs={'class': 'single-input'}),
            'email': forms.EmailInput(attrs={'class': 'single-input'}),
            'location': forms.TextInput(attrs={'class': 'single-input'}),
            
        }