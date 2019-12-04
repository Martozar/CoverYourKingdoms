from abc import ABC, abstractmethod

class Movable:
    def move(self, move_from, move_to):
        move_from.delete(self)
        move_to.add(self)

class Container:

    def __init__(self):
        self.container = []

    def __len__(self):
        return len(self.container)

class Expandable(Container):

    def __init__(self):
        super().__init__()

    def add(self, object):
        self.container.insert(0, object)


class Deletable(Container):
    def __init__(self):
        super().__init__()

    def delete(self, object):
        self.container = [o for o in self.container if o != object]


class ExpandableAndDeletable(Expandable, Deletable):

    def __init__(self):
        super().__init__()
