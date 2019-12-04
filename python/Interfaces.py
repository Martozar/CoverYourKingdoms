class Movable:
    def move(self, move_from, move_to):
        move_from.remove(self)
        move_to.insert(0, self)
