class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def character_name(self):
        print(self.name)

    def character_role(self):
        print(self.role)


class Player(Character):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.player_items = ['Sword']

    def show_items(self):
        print(f'{self.name} items :')
        for item in self.player_items:
            print(item)

    def use_item(self):
        for item in self.player_items:
            print(f'Używam{item}')


class Mag(Character):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.mag_items = ['Magic']

    def show_items(self):
        print(f'{self.name} items :')
        for item in self.mag_items:
            print(item)
