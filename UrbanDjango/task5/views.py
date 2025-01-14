from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import UserRegister

# Create your views here.

def sign_up_by_django(request):
    users = ['Mario', 'Luigi', 'Peach', 'Bowser', 'Toad', 'Link', 'Zelda', 'Ganondorf', 'Isabelle', 'Tom', 'Timmy', 'Tommy']
    form = UserRegister(request.POST)
    info = {}
    context = {
        'info': info,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeat_password and age >= 18:
                return HttpResponse(f'Приветствуем, {username}!')
            if username in users:
                return HttpResponse('Пользователь уже существует')
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            if age < 18:
                return HttpResponse('Вы должны быть старше 18 лет')
    return render(request, 'registration_page.html', info)