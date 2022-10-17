from django import forms
from .models import Adv

class AdvForm(forms.ModelForm):
    class Meta:
        model = Adv
        fields = ('name', 'description', 'photo',  'contact')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Дайте назву оголошенню'}),
            'description': forms.Textarea(attrs={'class': 'single-textarea', 'rows':6, 'placeholder': 'Опишіть детальніше оголошення'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'single-input'}),
            'contact': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'За необхідністю додайте контакти'}),
        }