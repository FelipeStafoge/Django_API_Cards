from django.shortcuts import render
from api import generate_a_card
from deck import deck_id

def index(request):
    return render(request, 'home/home.html')


def take_a_card(request):
    generate_a_card(deck_id)
    card, card_color, card_suit, card_value, json = generate_a_card(deck_id)
    print(json)
    return render(request, 'home/take_a_card.html',{'card_color': card_color, 'card_suit': card_suit, 'deck_id': deck_id, 
    'card_value': card_value})




