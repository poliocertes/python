class Room:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def room_name(self):
        print('\nYou are in: ')
        print(self.name)

    def location(self):
        return self.location


class First_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Magic Key', 'Magic Book']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name}: ')
        for item in self.items:
            print(item)

    def get_item(self):
        if item in self.items:
            Player.player_items.append(item)
            self.items.remove(item)


class Second_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Magic Bottle', 'Secret Key']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name} : ')
        for item in self.items:
            print(item)

    def get_item(self):
        if item in self.items:
            Player.player_items.append(item)
            self.items.remove(item)


class Last_chamber(Room):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.items = ['Gem']

    def show_items(self):
        print(f'\nPrzedmioty dostępne w {self.name} : ')
        for item in self.items:
            print(item)

    def get_item(self):
        if item in self.items:
            Player.player_items.append(item)
            self.items.remove(item)