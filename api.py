import requests
from deck import deck_id, deck, number



def shuffle(deck_id):
    reshuffle = f'https://www.deckofcardsapi.com/api/deck/{deck_id}/shuffle/'
    return requests.get(reshuffle)


def generate_a_card(deck_id):
    card = f'https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1'
    req = requests.get(card)
    json = req.json()
    card_value = json['cards'][0]['value']
    card_suit = json['cards'][0]['suit']
    card_image = json['cards'][0]['image']
    
    if json['remaining'] == 1:
        shuffle(deck_id)
    if card_suit == 'DIAMONDS' or card_suit == 'HEARTS':
        card_color = 'RED'
    else:
        card_color = 'BLACK'

    card_to_show = {
        'card_value': card_value,
        'card_suit': card_suit,
        'card_image': card_image
    }
    if len(deck) == 5:
        new_number = deck.all()[1]['number']
        new_number += 1
        deck.remove(doc_ids=[new_number])
        deck.update({"number": new_number},doc_ids=[2])

    deck.insert(card_to_show.copy())
    card_to_show.clear()
    return card, card_color, card_suit, card_value, card_image,json


def show_last_three():
    try:
        first_card = deck.all()[number['number']]
        second_card = deck.all()[number['number']+1]
        third_card = deck.all()[number['number']+2]
        error = None

    except(ValueError):
        error = 'ERROR. YOU GOT NOT ENOUGH CARDS'
    else:
        print(first_card, second_card, third_card)
        return error, first_card, second_card, third_card



