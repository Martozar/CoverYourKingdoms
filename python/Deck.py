from Interfaces import Deletable

class Deck(Deletable):

    def __init__(self):
        super().__init__()
        self.empty = False

    def initialize(self, cards_list: list):
        self.container = cards_list

    def isEmpty(self):
        return self.empty

    def draw(self):
        if self.empty:
            print("Nothing to draw!")
            return None
        card = self.container[0]
        self.delete(card)
        if len(self.container) == 0:
            print("Draw deck is empty")
            self.empty = True
        return card
