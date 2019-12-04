class Deck:

    def __init__(self):
        self.cards = list()
        self.empty = False

    def initialize(self, cards_list: list):
        self.cards = cards_list

    def isEmpty(self):
        return self.empty

    def draw(self):
        if self.empty:
            print("Nothing to draw!")
            return None
        card = self.cards[0]
        if len(self.cards) == 0:
            print("Draw deck is empty")
            self.empty = True
        return card
