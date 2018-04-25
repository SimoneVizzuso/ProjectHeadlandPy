from adventure.player import Player
import world


def play():
    world.load_rooms()
    player = Player()
    room = world.room_exists(player.position_x, player.position_y)
    print(room.intro())
    while player.is_alive() and not player.victory:
        room = world.room_exists(player.position_x, player.position_y)
        print("Choose an action:\n")
        available_actions = room.available_actions()
        for action in available_actions:
            print(action)
        action_input = input('Action: ')
        for action in available_actions:
            if action_input == action.hotkey:
                player.action(action, **action.kwargs)
                break


if __name__ == "__main__":
    play()
