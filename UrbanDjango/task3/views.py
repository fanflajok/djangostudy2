from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
def shop(request):
    title = 'Игры'
    game1 = 'Super Mario Odyssey 2'
    game2 = 'The Legend of Zelda: The Wind Waker HD remake'
    game3 = "Luigi's Mansion 4"
    game4 = 'Pikmin 5'
    game5 = 'Mario Cart 9'
    game6 = 'Splatoon 6'
    game7 = "Yoshi's Super World"
    game8 = 'Kirby and the Forgotten Land 2'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'game4': game4,
        'game5': game5,
        'game6': game6,
        'game7': game7,
        'game8': game8,
    }
    return render(request, 'shop.html', context)
def cart(request):
    text = 'Вы ничего не положили в корзину'
    context = {'text':text}
    return render(request, 'cart.html',context)