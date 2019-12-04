from Card import CreatureCard
from Interfaces import Movable


class Clan(Movable):

    def __init__(self):
        super().__init__()
        self.creatures = list()

    def get_value(self):
        value = 0
        for creature in self.creatures:
            value+=creature.value
        return value


class Kindgom:

    def __init__(self, name):
        self.clans = list()
        self.name = name

    def add_clan(self, clan):
        self.clans.insert(0, clan)
        clan.location = self

    def get_points(self):
        value = 0
        for clan in self.clans:
            value+=clan.get_value()
        return value
