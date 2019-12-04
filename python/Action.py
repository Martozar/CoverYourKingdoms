import Game
print("Actions")
from Player import Player
from Card import Card
import sys
from abc import ABC, abstractmethod

class Action(ABC):

    @abstractmethod
    def take_action(game: Game, target_player: Player, card: Card):
        pass

    @abstractmethod
    def isAvailable(game: Game, target_player: Player):
        pass


class DiscardAndDraw(Action):

    def isAvailable(game: Game, target_player=None):
        if game.current_player.emptyHand():
            return False
        return True

    def take_action(game: Game, target_player=None):
        print("Which card you want to discard?")
        print(game.current_player.hand)
        card = int(sys.stdin.readline())
        game.current_player.discard(game.discard_pile, card)
        print(game.current_player.hand)

class CreateClanAction(Action):

    def isAvailable(game: Game, target_player=None):
        for i in range(len(game.current_player.hand)):
            for j in range(i+1, len(game.current_player.hand)):
                if game.current_player.hand[i].name == game.current_player.hand[j].name:
                    return True
        return False

    def take_action(game: Game, target_player=None):
        print("Available creatures: ")
        print(game.current_player.hand)
        print("Chose 2 different creatures with the same name")
        while True:
            creatures = sys.stdin.readline().split(" ")
            if len(creatures) != 2:
                print("Chose 2 creatures!")
                continue
            creatures = [int(creatures[i]) for i in range(len(creatures))]
            if creatures[0] == creatures[1]:
                print("Chose different creatures!")
                continue
            if game.current_player.hand[creatures[0]].name != game.current_player.hand[creatures[1]].name:
                print("Not the creatures with the same name!")
                continue
            else:
                break
        game.current_player.add_clan([game.current_player.hand[creatures[0]], game.current_player.hand[creatures[1]]])
        game.current_player.hand = [game.current_player.hand[i] for i in range(len(game.current_player.hand)) if i not in creatures]
