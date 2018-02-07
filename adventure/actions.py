from player import Player


class Action():
    def __init__(self, method, name, hotkey, **other):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.other = other

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='N')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='S')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='E')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='W')


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='I')


class ViewObjectDescription(Action):
    def __init__(self):
        super().__init__(method=Player.view_object_description, name='View Object Description', hotkey='D')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='A', enemy=enemy)
