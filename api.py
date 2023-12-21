import requests
from deck import deck_id


def shuffle(deck_id):
    reshuffle = f'https://www.deckofcardsapi.com/api/deck/{deck_id}/shuffle/'
    return requests.get(reshuffle)


def generate_a_card(deck_id):
    card = f'https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1'
    req = requests.get(card)
    json = req.json()
    card_value = json['cards'][0]['value']
    card_suit = json['cards'][0]['suit']
    
    if json['remaining'] == 1:
        shuffle(deck_id)
    if card_suit == 'DIAMONDS' or card_suit == 'HEARTS':
        card_color = 'RED'
    else:
        card_color = 'BLACK'
    return card, card_color, card_suit, card_value, json

