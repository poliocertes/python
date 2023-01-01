class Item:
    def __init__(self, name, power_impact):
        self.name = name
        self.power_impact = power_impact

    def show_name(self):
        print(self.name)

    def power_impact(self):
        return self.power_impact

class Magic_key(Item):
    def use_key(self):
        print('Używam magiczny klucz.')

class Magic_book(Item):
    def use_magic_book(self):
        print('Uzywam magiczną książkę')

class Secret_key(Item):
    def use_secret_key(self):
        print('Używam sekretny klucz')

class Magic_bottle(Item):
    def use_magic_bottle(self):
        print('Używam magicznej butelki')

class Gem(Item):
    def get_gem(self):
        print('Gem zdobyty!')

