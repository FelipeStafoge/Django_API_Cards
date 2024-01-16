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
    deck.insert(card_to_show.copy())
    card_to_show.clear()
    if len(deck.all()) > 5:
        deck.remove(doc_ids=[number["number"]])
        number['number'] += 1
        deck.update(
            {'number': number['number']},
            doc_ids=[2]
        )



    

    return card, card_color, card_suit, card_value, card_image,json


def show_last_three():
    try:
        first_card = last_three[0]
        second_card = last_three[1]
        third_card = last_three[2]
    except:
        print('You got not enough cards')
    print('vasco')



