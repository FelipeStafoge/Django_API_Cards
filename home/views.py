from django.shortcuts import render
from api import generate_a_card, show_last_three
from deck import deck_id

def index(request):
    return render(request, 'home/home.html', {'title': 'Home'})


def take_a_card(request):
    card, card_color, card_suit, card_value, card_image,json= generate_a_card(deck_id)
    print(json)
    print('//////////////////////////////////')

    return render(request, 'home/take_a_card.html',{'card_color': card_color, 'card_suit': card_suit, 'deck_id': deck_id, 
    'card_value': card_value, 'card_image': card_image, 'title': 'Take a card'})

def last_three_cards(request):
    error, first_card, second_card, third_card = show_last_three()
    first_card_value = first_card['card_value']
    first_card_suit = first_card['card_suit']
    first_card_image = first_card['card_image']

    second_card_value = second_card['card_value']
    second_card_suit = second_card['card_suit']
    second_card_image = second_card['card_image']

    third_card_value = third_card['card_value']
    third_card_suit = third_card['card_suit']
    third_card_image = third_card['card_image']

    return render(request, 'home/last_three_cards',{'title': 'Last three', 'error': error, 'first_card_value': first_card_value, 
    'first_card_suit': first_card_suit, 'first_card_image': first_card_image, 'second_card_value': second_card_value,
    'second_card_suit': second_card_suit, 'second_card_image': second_card_image, 'third_card_value': third_card_value, 
    'third_card_suit': third_card_suit, 'third_card_image': third_card_image})