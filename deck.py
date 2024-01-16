import requests
from tinydb import TinyDB, Query

deck = TinyDB('deck.json', indent=4)
consult = Query()

number = {
    'number': 3
}


if len(deck) == 0:
    url_new_deck = 'https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
    req = requests.get(url_new_deck)
    json = req.json()
    deck.insert(json)
    deck.insert(number)
    deck_id = json['deck_id']


deck_id = deck.all()[0]['deck_id']


