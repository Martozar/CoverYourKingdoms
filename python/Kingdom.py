from Card import CreatureCard
from Interfaces import Movable, Expandable


class Clan(Movable, Expandable):

    def __init__(self, creature_cards: list):
        self.container = creature_cards

class Kindgom(Expandable):

    def __init__(self, name):
        super().__init__()
        self.name = name
