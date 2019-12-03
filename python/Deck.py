class Deck:

    def __init__(self):
        self.cards = []

    def initialize(self, cards_list: list):
        self.cards = cards_list

    def draw(self):
        if len(self.cards) == 0:
            print("Draw deck is empty")
            return None
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card
