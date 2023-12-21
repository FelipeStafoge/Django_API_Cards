import requests
from tinydb import TinyDB

deck = TinyDB('deck.json')



if len(deck) == 0:
    url_new_deck = 'https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
    req = requests.get(url_new_deck)
    json = req.json()
    deck.insert(json)
    deck_id = json['deck_id']


deck_id = deck.all()[0]['deck_id']


