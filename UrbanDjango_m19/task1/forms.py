from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    email = forms.EmailField(label='Введите Email', max_length=100)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль")
    age = forms.IntegerField(max_value=999, min_value=0, label="Введите свой возраст")