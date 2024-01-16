from django.shortcuts import render
from api import generate_a_card
from deck import deck_id

def index(request):
    return render(request, 'home/home.html', {'title': 'Home'})


def take_a_card(request):
    card, card_color, card_suit, card_value, card_image,json= generate_a_card(deck_id)
    print(json)
    print('//////////////////////////////////')

    print('//////////////////////////////////')
    return render(request, 'home/take_a_card.html',{'card_color': card_color, 'card_suit': card_suit, 'deck_id': deck_id, 
    'card_value': card_value, 'card_image': card_image, 'title': 'Take a card'})

def last_three_cards(request):
    return render(request, 'home/last_three_cards',{'title': 'Last three'})