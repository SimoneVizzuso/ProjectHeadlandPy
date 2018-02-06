__author__ = 'SimoneVizzuso and GabrieleLavorato'
import items


class Player:
    def __init__(self):
        self.inventory = [items.Sword(), items.Rock(), items.OldMap()]
        self.hp = 100
        self.victory = False

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def is_alive(self):
        return self.hp > 0


