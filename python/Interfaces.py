class Movable:

    def __init__(self):
        self.location = None

    def move(self, move_from, move_to, move_to_index=0):
        move_from.remove(self)
        move_to.insert(move_to_index, self)
        self.location = move_to
