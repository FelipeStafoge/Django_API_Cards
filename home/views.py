from django.shortcuts import render
from api import generate_a_card, show_last_three 
from deck import deck_id

def index(request):
    return render(request, 'home/home.html')


def take_a_card(request):
    card, card_color, card_suit, card_value, card_image,json = generate_a_card(deck_id)
    print(json)
    print('//////////////////////////////////')
    show_last_three()
    print('//////////////////////////////////')
    return render(request, 'home/take_a_card.html',{'card_color': card_color, 'card_suit': card_suit, 'deck_id': deck_id, 
    'card_value': card_value, 'card_image': card_image})

def last_three_cards(request):
    first_card, second_card, third_card = show_last_three()
    print(first_card)
    show_last_three()
    return render(request, 'home/last_three_cards', {'first_card':first_card, 'second_card':second_card, 'third_card':third_card})