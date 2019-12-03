from Deck import Deck
from Kingdom import Kindgom, Clan
class Player:

    def __init__(self):
        self.hand = [] # array of cards
        self.kingdom  = None

    def set_kingdom(self, name):
        self.kingdom = Kindgom(name)

    def draw(self, deck: Deck):
        self.hand.append(deck.draw())

    def replenish_hand(self, deck):
        for _ in range(6 - len(self.hand)):
            self.draw(deck)
            
    def draw_oppenning(self, deck: Deck):
        for i in range(6):
            self.draw(deck)

    def add_clan(self, creatures: list):
        self.kingdom.add_clan(Clan(creatures))
