from Deck import Deck
from Kingdom import Kindgom, Clan
from Interfaces import ExpandableAndDeletable

class Player:

    def __init__(self):
        self.hand = ExpandableAndDeletable() # array of cards
        self.kingdom  = None

    def set_kingdom(self, name):
        self.kingdom = Kindgom(name)

    def draw(self, deck: Deck):
        self.hand.add(deck.draw())

    def discard(self, discard_pile, card_number):
        discard_pile.discard(self.hand[card_number])
        self.hand = [self.hand[i] for i in range(len(self.hand)) if i != card_number]


    def replenish_hand(self, deck):
        for _ in range(6 - len(self.hand)):
            self.draw(deck)

    def draw_oppenning(self, deck: Deck):
        for i in range(6):
            self.draw(deck)

    def emptyHand(self):
        return len(self.hand) == 0

    def add_clan(self, creatures: list):
        self.kingdom.add_clan(Clan(creatures))
