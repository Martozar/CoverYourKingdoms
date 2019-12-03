from Player import Player
import sys
from abc import ABC, abstractmethod
class Action(ABC):

    @abstractmethod
    def take_action(player1: Player, player2: Player):
        pass

    @abstractmethod
    def isAvailable(player1: Player, player2: Player):
        pass

class CreateClanAction(Action):

    def isAvailable(player1: Player, player2=None):
        for i in range(len(player1.hand)):
            for j in range(i+1, len(player1.hand)):
                if player1.hand[i].name == player1.hand[j].name:
                    return True
        return False

    def take_action(player1: Player, palyer2=None):
        print("Available creatures: ")
        print(player1.hand)
        print("Chose 2 different creatures with the same name")
        while True:
            creatures = sys.stdin.readline().split(" ")
            if len(creatures) != 2:
                print("Chose 2 creatures!")
                continue
            if int(creatures[0]) == int(creatures[1]):
                print("Chose different creatures!")
                continue
            if player1.hand[int(creatures[0])].name != player1.hand[int(creatures[1])].name:
                print("Not the creatures with the same name!")
                continue
            else:
                break
        player1.add_clan([player1.hand[int(creatures[0])], player1.hand[int(creatures[1])]])
        player1.hand = [player1.hand[i] for i in range(len(player1.hand)) if i != int(creatures[0]) and i != int(creatures[1])]
