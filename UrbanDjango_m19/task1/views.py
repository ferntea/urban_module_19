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
    games = Game.objects.all()

    # Pagination
    paginator = Paginator(games, 3)  # 3 games/page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'games': page_obj}
    return render(request, 'first_task/shop.html', context)

def cart_view(request):
    return render(request, 'first_task/cart.html')
