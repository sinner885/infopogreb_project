from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Service, Coment

class ServiceForm(forms.ModelForm):
    
    description = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class': 'single-input', 'rows':6}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "категорія не вибрана"
    
    class Meta:
        model = Service
        fields = ('category', 'brend', 'subject', 'description', 'images', 'name', 'telefon', 'email', 'location')
        widgets = {
            'category': forms.Select(attrs={'class': 'single-input'}),
            'brend': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'назва фірми, компанії, магазину і т.п.'}),
            'subject': forms.TextInput(attrs={'class': 'single-input'}),
            'slug': forms.TextInput(attrs={'class': 'single-input'}),
            #'description': forms.Textarea(attrs={'class': 'single-input', 'rows':6}),
            'images': forms.ClearableFileInput(attrs={'class': 'single-input'}),
            'name': forms.TextInput(attrs={'class': 'single-input'}),
            'telefon': forms.TextInput(attrs={'class': 'single-input', 'placeholder': '(xxx xxx xx xx)'}),
            'email': forms.EmailInput(attrs={'class': 'single-input'}),
            'location': forms.TextInput(attrs={'class': 'single-input'}),
            
        }
        
        
class ComentForm(forms.ModelForm):
    class Meta:
        model = Coment
        
        fields = ('coment',)
        widgets = {
            'coment': forms.Textarea(attrs={'class': 'single-textarea', 'rows':6, 'placeholder': 'Поділіться своїм враженням від наданої послуги.'}),
        }
        labels = {
            'coment': '',
        }