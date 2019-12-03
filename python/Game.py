from Card import Card, CreatureCard, CreatureType
from Player import Player
from Deck import Deck
from Action import CreateClanAction

import random
import string
import sys

creatures = [CreatureCard("1", 5, CreatureType.COMMON, None), CreatureCard("2", 10, CreatureType.COMMON, None)]

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

players = []
player1 = Player()
players.append(player1)
player1.set_kingdom(randomString)
card_list = [creatures[random.randint(0, 1)] for i in range(60)]
deck = Deck()
deck.initialize(card_list)
player1.draw_oppenning(deck)


# while True:
print("What action you want to take?")
print("1 - create clan")
line = sys.stdin.readline()
if int(line) == 1:
    if CreateClanAction.isAvailable(player1):
        CreateClanAction.take_action(player1)
print("Replenishing all players hand")
for p in players:
    p.replenish_hand(deck)
