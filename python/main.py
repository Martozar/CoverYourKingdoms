from Game import Game
from Player import  Player
from Deck import Deck
from Card import CreatureCard, CreatureType
import random
import string
import copy

creatures = [CreatureCard("1", 5, CreatureType.COMMON, None), CreatureCard("2", 10, CreatureType.COMMON, None)]

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

players = []
player1 = Player()
players.append(player1)
player1.set_kingdom(randomString)

card_list = [copy.deepcopy(creatures[random.randint(0, 1)]) for i in range(60)]
deck = Deck()
deck.initialize(card_list)

g = Game()
g.initialize(deck, players)
g.mainLoop()
