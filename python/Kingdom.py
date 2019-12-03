from Card import CreatureCard


class Clan:

    def __init__(self, creature_cards: list):
        self.creatures = creature_cards

    def add(self, creature_card: CreatureCard):
        self.creatures.insert(0, creature_card)
        
class Kindgom:

    def __init__(self, name):
        self.name = name
        self.clans = []

    def add_clan(self, clan: Clan):
        self.clans.insert(0, clan)
