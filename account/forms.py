from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MyUser

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password kiriting',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password kiriting'})
    )
    password2 = forms.CharField(label='Password qayta kiriting',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password qayta kiriting'})
    )

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email kiriting'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number kiriting'}),
        }

class UserEditForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'img', 'bio', 'phone', 'birth_day']