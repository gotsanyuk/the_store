from django import forms
from django.core.validators import RegexValidator
from .models import Order


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class OrderCreateForm(forms.ModelForm):

    # VALIDATIONS
    first_name = forms.CharField(
        label='Ваше імʼя', min_length=2, max_length=30,
        validators= [RegexValidator(r'^[а-яіїґА-ЯІЇҐ]*$',
        message='Вас справді так звати?')],
        widget=forms.TextInput(attrs={'placeholder': 'Введіть своє імʼя'})
    )
    last_name = forms.CharField(
        label='Ваше прізвище', min_length=2, max_length=30,
        validators= [RegexValidator(r'^[а-яіїґА-ЯІЇҐ]*$',
        message='У вас справді таке прізвище?')],
        widget=forms.TextInput(attrs={'placeholder': 'Введіть своє прізвище'})
    )
    email = forms.CharField(
        label='Ваш email', min_length=7, max_length=40,
        validators= [RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message='Це скоріш за все не та пошта')],
        widget=forms.TextInput(attrs={'placeholder': 'Введіть свою електронну адресу'})
    )
    address = forms.CharField(
        label='Адреса доставки', min_length=2, max_length=50,
        validators= [RegexValidator(r'[а-яіїґА-ЯІЇҐ\s]*',
        message='Куди ця адреса заведе?')],
        widget=forms.TextInput(attrs={'placeholder': 'Введіть адресу доставки'})
    )
    city = forms.CharField(
        label='Область', min_length=2, max_length=30,
        validators= [RegexValidator(r'^[а-яіїґА-ЯІЇҐ-]*$',
        message='Одним словом')],
        widget=forms.TextInput(attrs={'placeholder': 'Введіть свою область'})
    )
  
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',  'city']