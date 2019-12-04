from Deck import Deck
from Kingdom import Kindgom, Clan

class Player:

    def __init__(self):
        self.hand = list() # array of cards
        self.kingdom  = None

    def set_kingdom(self, name):
        self.kingdom = Kindgom(name)

    def get_points(self):
        return self.kingdom.get_points()

    def draw(self, deck: Deck):
        card = deck.draw()
        if card:
            card.move(deck.cards, self.hand)

    def discard(self, discard_pile, card):
        card.move(self.hand, discard_pile)

    def replenish_hand(self, deck):
        for _ in range(6 - len(self.hand)):
            self.draw(deck)

    def emptyHand(self):
        return len(self.hand) == 0

    def add_clan(self, creatures: list):
        clan = Clan()
        for c in creatures:
            c.move(c.location, clan.creatures)
        self.kingdom.add_clan(clan)
