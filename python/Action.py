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
    def undo(game: Game, target_player: Player, card: Card):
        pass

    @abstractmethod
    def isAvailable(game: Game, target_player: Player):
        pass

    @abstractmethod
    def getName():
        pass


class AddCreature(Action):

    def getName():
        return "Add Creature"

    def isAvailable(game: Game, target_player=None):
        if not game.current_player.kingdom.clans:
            return False
        for c in game.current_player.hand:
            if c.name == game.current_player.kingdom.clans[0].creatures[0].name:
                return True
        return False

    def take_action(game: Game, target_player=None, card=None):
        available = [c for c in game.current_player.hand if c.name == game.current_player.kingdom.clans[0].creatures[0].name]
        print("Which card you want to add?")
        print(available)
        card = int(sys.stdin.readline())
        card = available[card]
        card.move(card.location, game.current_player.kingdom.clans[0].creatures, 1)


class DiscardAndDraw(Action):

    def getName():
        return "Discard And Draw"

    def isAvailable(game: Game, target_player=None):
        if game.current_player.emptyHand():
            return False
        return True

    def take_action(game: Game, target_player=None, card=None):
        print("Which card you want to discard?")
        print(game.current_player.hand)
        card = int(sys.stdin.readline())
        game.current_player.discard(game.discard_pile, game.current_player.hand[card])
        print(game.current_player.hand)
        game.current_player.draw(game.deck)
        print(game.current_player.hand)


class CreateClanAction(Action):

    def getName():
        return "Create Clan Action"

    def isAvailable(game: Game, target_player=None):
        for i in range(len(game.current_player.hand)):
            for j in range(i+1, len(game.current_player.hand)):
                if game.current_player.hand[i].name == game.current_player.hand[j].name:
                    return True
                if game.discard_pile and game.current_player.hand[i].name == game.discard_pile[0]:
                    return True
        return False

    def take_action(game: Game, target_player=None):
        print("Chose 2 different creatures with the same name")
        chosen = []
        available = []
        while len(chosen) < 2:
            if len(chosen) == 0:
                print("Choose a card in your hand:")
                print(game.current_player.hand)
                card = int(sys.stdin.readline())
                chosen.append(game.current_player.hand[card])
                available = game.current_player.hand + ([] if not game.discard_pile else [game.discard_pile[0]])
                available = [c for c in available if c.name == chosen[0].name and c != chosen[0]]
                if not available:
                    print("Choose another creature!")
                    chosen = []
                    continue
            if len(chosen) == 1:
                print("Choose a card in your hand{}:".format("" if not game.discard_pile else " or discard_pile"))
                print(available)
                card = int(sys.stdin.readline())
                chosen.append(available[card])
            if len(chosen) == 2:
                game.current_player.add_clan([chosen[0], chosen[1]])
            # creatures = [int(creatures[i]) for i in range(len(creatures))]
            # if creatures[0] == creatures[1]:
            #     print("Chose different creatures!")
            #     continue
            # if game.current_player.hand[creatures[0]].name != game.current_player.hand[creatures[1]].name:
            #     print("Not the creatures with the same name!")
            #     continue
            # else:
            #     break
