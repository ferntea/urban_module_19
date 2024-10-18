from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister

# Sample list of existing users (consider using a database in a real application)
users = ['Ann', 'Anton', 'Peter']

template_name = 'first_task/registration_page.html'

def sign_up_by_html(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                form.add_error('username', 'Пользователь уже существует')
            elif password != password_repeat:
                form.add_error('repeat_password', 'Пароли не совпадают')
            elif age < 18:
                form.add_error('age', 'Вы должны быть старше 18')
            else:
                # Here you can add the user to your database
                # For example: User.objects.create_user(username=username, email=email, password=password)
                return redirect('home')  # Redirect to home after successful registration

    return render(request, template_name, {'form': form})

def home(request):
    return render(request, 'first_task/home.html')

def shop_view(request):
    return render(request, 'first_task/shop.html')

def cart_view(request):
    return render(request, 'first_task/cart.html')
