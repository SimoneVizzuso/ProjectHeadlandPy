__author__ = 'SimoneVizzuso and GabrieleLavorato'


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}\n=====\n{}'.format(self.name, self.description)


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        return '{}\n=====\n{}\nDamage: {}'.format(self.name, self.description, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name='Rock',
                         description='A rock that you found in your bag',
                         damage=5)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name='Sword',
                         description='An old and ruined sword that can still kill some enemy',
                         damage=15)


class OldMap(Item):
    def __init__(self):
        super().__init__(name='Old Map',
                         description='The exit is north but you must first explore the dungeon\nTo the west you could '
                                     'find something very powerful\nYou will have to go east, but beware of the '
                                     'danger')
