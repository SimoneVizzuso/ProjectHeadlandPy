import world, items
from adventure.items import LifeScroll, DamageScroll

__author__ = "SimoneVizzuso and GabrieleLavorato"


class Player:
    def __init__(self):
        self.inventory = [items.Stick()]
        self.hp = 100
        self.position_x, self.position_y = world.starting_position
        self.victory = False

    def print_inventory(self):
        for item in self.inventory:
            print(item, "\n")

    def action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def is_alive(self):
        return self.hp > 0

    def view_inventory(self):
        for item in self.inventory:
            print(item, "\n")

    def move(self, dx, dy):
        self.position_x = self.position_x + dx
        self.position_y = self.position_y + dy
        print(world.room_exists(self.position_x, self.position_y).intro())

    def move_north(self):
        self.move(dx = 0, dy = -1)

    def move_south(self):
        self.move(dx = 0, dy = 1)

    def move_east(self):
        self.move(dx = 1, dy = 0)

    def move_west(self):
        self.move(dx = -1, dy = 0)

    #def attack(self):
        #something

    def use_item(self, enemy):
        if LifeScroll() in self.inventory or DamageScroll() in self.inventory:
            print("which object you want to use?\n")
            if LifeScroll() in self.inventory:
                print("Use Life Scroll - to heal yourself")
            if DamageScroll() in self.inventory:
                print("Use Damage Scroll - to harm your enemy")
            print("Back - go to the previous choice")

            action = input("Action: ")
            choice = 0

            while (choice == 0):
                if action == "Use Life Scroll":
                    self.hp = 100
                    pos = self.inventory.index(LifeScroll())
                    del self.inventory[pos]
                    choice = 1
                elif action == "Use Damage Scroll":
                    enemy.hp = enemy.hp - 50
                    pos = self.inventory.index(DamageScroll())
                    del self.inventory[pos]
                    choice = 1
                elif action == "back":
                    choice = 1