_world = {}
start = (0, 0)


def room_exists(x, y):
    return _world.get((x, y))


def load_tiles():
    with open('adventureMap.txt', 'r') as f:
        rows = f.readlines()
    for k in range(len(rows)):
        cols = rows[k].split(' ')
        room_name = cols[0].replace('\n', '')
        y = cols[1]
        x = cols[2]
        if room_name == 'Start':
            global start
            start = (x, y)
        _world[(x, y)] = None if room_name == '' else getattr(__import__('rooms'), room_name)(x, y)
