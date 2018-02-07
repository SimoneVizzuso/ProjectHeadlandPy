class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=20, damage=5)


class Golem(Enemy):
    def __init__(self):
        super().__init__(name="Golem", hp=50, damage=20)

class Dragon(Enemy):
    def __init__(self):
        super().__init__(name="Dragon", hp=100, damage=30)