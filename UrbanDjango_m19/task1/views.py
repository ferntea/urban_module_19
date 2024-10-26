from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer, Game
from django.core.paginator import Paginator

# Sample list of existing users
# users = ['Ann', 'Anton', 'Peter']

template_name = 'first_task/register.html'

def sign_up_by_html(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']  # Assuming you'll use email
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name__iexact=username).exists():
                form.add_error('username', 'Пользователь уже существует')
            elif password != password_repeat:
                form.add_error('repeat_password', 'Пароли не совпадают')
            elif age < 18:
                form.add_error('age', 'Вы должны быть старше 18')
            else:
                # Create a new Buyer
                new_buyer = Buyer.objects.create(
                    name=username,
                    balance=0.00,  # initial balance
                    age=age,
                    email=email     # added
                )
                return redirect('home')

    return render(request, template_name, {'form': form})

def home(request):
    return render(request, 'first_task/home.html')

from django.shortcuts import render
from .models import Game


def shop_view(request):
    items_per_page = request.GET.get('items_per_page', '3')  # Default to 5
    items_per_page = int(items_per_page) if items_per_page.isdigit() else 3

    games = Game.objects.all()
    paginator = Paginator(games, items_per_page)  # Create a paginator object

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the current page

    return render(request, 'first_task/game_list.html', {
        'page_obj': page_obj,
        'items_per_page': items_per_page,
        'games': games  # Pass the full list of games if needed
    })


def cart_view(request):
    return render(request, 'first_task/cart.html')

