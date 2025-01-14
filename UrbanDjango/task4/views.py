from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def shop(request):
    title = 'Игры'
    list_of_games = ['Super Mario Odyssey 2', 'The Legend of Zelda: The Wind Waker HD remake', "Luigi's Mansion 4", 'Pikmin 5',
                  'Mario Cart 9', 'Splatoon 6', "Yoshi's Super World", 'Kirby and the Forgotten Land 2'
                  ]
    context = {
        'title': title,
        'list': list_of_games
    }
    return render(request, 'shop.html', context)
def cart(request):
    return render(request, 'cart.html')