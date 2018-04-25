import world, actions


def control(room):
    if room == "SecondLeverRoom":
        print("Some bars block your passage to the East")
        return False
    if room == "LogicGameRoom":
        print("Some bars block your passage to the West")
        return False
    if room == "EndRoom":
        print("You can not escape to your fate")


class MapRoom:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro(self):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.room_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.room_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.room_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.room_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartRoom(MapRoom):
    def intro(self):
        return "\nStart Room"


class EmptyRoom(MapRoom):
    def intro(self):
        return "\nEmpty Room"


class WeaponRoom(MapRoom):
    def intro(self):
        return "\nWeapon Room"


class OldMapRoom(MapRoom):
    def intro(self):
        return "\nOld Map Room"


class FirstLeverRoom(MapRoom):
    def intro(self):
        return "\nFirst Lever Room"


class SecondLeverRoom(MapRoom):
    def intro(self):
        return "\nSecond Lever Room"


class GoblinRoom(MapRoom):
    def intro(self):
        return "\nGoblin Room"


class GolemRoom(MapRoom):
    def intro(self):
        return "\nGolem Room"


class LogicGameRoom(MapRoom):
    def intro(self):
        return "\nLogic Room"


class EndRoom(MapRoom):
    def intro(self):
        return "\nEnd Room"
