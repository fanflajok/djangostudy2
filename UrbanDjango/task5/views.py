from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import UserRegister
users = ['Mario', 'Luigi', 'Peach', 'Bowser', 'Toad', 'Link', 'Zelda', 'Ganondorf', 'Isabelle', 'Tom', 'Timmy', 'Tommy']
# Create your views here.

def sign_up_by_django(request):
    form = UserRegister(request.POST)
    info = {}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeat_password and age >= 18:
                return HttpResponse(f'Приветствуем, {username}!')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
    return render(request, 'registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username not in users and password == repeat_password and age >= 18:
            return HttpResponse(f'Приветствуем, {username}!')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
    return render(request, 'registration_page.html', info)
