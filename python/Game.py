from Card import Card, CreatureCard, CreatureType
from Player import Player
from Deck import Deck

import sys
import Action
print("Game")

class Game:

    def __init__(self):
        self.current_player = None
        self.deck = None
        self.discard_pile = list()
        self.players = []
        self.actions = [Action.AddCreature, Action.CreateClanAction, Action.DiscardAndDraw]

    def initialize(self, deck, players):
        self.deck = deck
        self.players = players
        for p in self.players:
            p.replenish_hand(self.deck)

    def isFinished(self):
        if self.deck.isEmpty():
            for player in self.players:
                if len(player.hand) > 0:
                    return False
            return True
        return False

    def availableActions(self):
        available = []
        for action in self.actions:
            if action.isAvailable(self):
                available.append(action)
        return available



    def mainLoop(self):
        while not self.isFinished():
            for player in self.players:
                self.current_player = player
                print("What action you want to take?")
                available = self.availableActions()
                for i, action in enumerate(available):
                    print('{} - {}'.format(i, action.getName()))
                line = int(sys.stdin.readline())
                available[line].take_action(self)
                # if int(line) == 1:
                #     if Action.CreateClanAction.isAvailable(self):
                #         Action.CreateClanAction.take_action(self)
                # if int(line) == 2:
                #     if Action.DiscardAndDraw.isAvailable(self):
                #         Action.DiscardAndDraw.take_action(self)
                # if int(line) == 3:
                #     if Action.AddCreature.isAvailable(self):
                #         Action.AddCreature.take_action(self)
                print("Replenishing all players hand")
                for p in self.players:
                    p.replenish_hand(self.deck)
                print(player.get_points())



# while True:
