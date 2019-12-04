from Ability import Ability
from enum import Enum
from Interfaces import Movable

class CreatureType(Enum):
    COMMON = 1
    WILD = 2
    SPECIAL = 3


class Card(Movable):

    def __init__(self, name: str, location=None):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class CreatureCard(Card):

    def __init__(self, name: str, value: int, type: CreatureType, ability: Ability, location=None):
        super().__init__(name, location)
        self.value = value
        self.ability = ability
        self.type = type

    def __str__(self):
        return self.name + ", Magical Value: " + str(self.value)

    def __repr__(self):
        return self.__str__()
