from Card import CreatureCard
from Interfaces import Movable


class Clan(Movable):

    def __init__(self):
        self.creatures = list()


class Kindgom:

    def __init__(self, name):
        self.clans = list()
        self.name = name

    def add_clan(self, clan):
        self.clans.insert(0, clan)
