from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Advert

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'single-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'single-input'}))



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'single-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'single-input', 'placeholder': 'Email adress'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'single-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'single-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class AdvertForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "категорія не вибрана"
        
    
    
    class Meta:
        model = Advert
        fields = ('category', 'subject', 'types_ad', 'types_pr', 'description', 'images', 'price', 'name', 'email', 'telefon', 'location')
        widgets = {
            'category': forms.Select(attrs={'class': 'single-input'}),
            'subject': forms.TextInput(attrs={'class': 'single-input'}),
            'slug': forms.TextInput(attrs={'class': 'single-input'}),
            'types_ad': forms.Select(attrs={'class': 'single-input'}),
            'types_pr': forms.Select(attrs={'class': 'single-input'}),
            'description': forms.Textarea(attrs={'class': 'single-input', 'rows':6}),
            'images': forms.ClearableFileInput(attrs={'class': 'single-input'}),
            'price': forms.NumberInput(attrs={'class': 'single-input'}),
            'name': forms.TextInput(attrs={'class': 'single-input'}),
            'email': forms.EmailInput(attrs={'class': 'single-input'}),
            'telefon': forms.TextInput(attrs={'class': 'single-input'}),
            'location': forms.TextInput(attrs={'class': 'single-input'}),
            
            
            
        }
    
    
        
        