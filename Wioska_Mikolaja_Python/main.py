# Santa Claus village in Python OOP

class Village:
    max_buildings = 20
    population = 0

    def __init__(self, village_name, population, max_buildings):
        self.village_name = village_name
        self.population = population
        self.max_buildings = max_buildings

    def get_name(self):
        return self.village_name

    def show_population(self):
        return self.population

    def create_building(self, building):
        if len(Village.buildings) < self.max_buildings:
            Building.buildings.append(building)

class Building(Village):
    def __init__(self, max_buildings, house_name, owner, max_residents):
        super().__init__(max_buildings)
        self.house_name = house_name
        self.owner = owner
        self.buildings = []
        self.store = False
        self.max_residents = max_residents

    def localization(self, village):
        print(f"This is a {self.house_name} in the {village.name} village.")

    def show_items(self): 
        for item in items:
            print(item)

class Resident(Village):
    def __init__(self, name, role, age, owner, population):
        super().__init__(population, owner)
        self.name = name
        self.role = role
        self.age = age

    def add_resident(self):
        if not self.store:
            self.store = False
            Village.population.append(self.resident)

    def take_building(self, owner):
        self.building.owner = owner

class Item(Building):
    def __init__(self, name, color, store):
        super().__init__(store)
        self.name = name
        self.color = color
        self.items = []

    def add_item(self):
        if not self.store:
            self.items.append(self.item)

class Magical_Charakters(Resident):
    def __init__(self, name, role, age):
        super().__init__(name, role, age)
        self.ability = ability

    def show_ability(self):
        return self.ability

class Animal(Resident):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.reindeer = True
        self.power = power

    def show_power_level(self):
        return self.power

class Gifts(Item):
    def __init__(self, name, adress, weight):
        super().__init__(name)
        self.adress = adress
        self.weight = weight

    def send_gift(self):
        location = str(self.adress) + str(self.name)

class Santa_Claus(Resident):
    def __init__(self, name, role, age, width, height):
        super().__init__(name, role, age)
        self.sleep = False
        self.width = width
        self.height = height
        self.tired = True

    def say_something(self):
        print('Ha-ha-ha-ha :)')

class Elf(Magical_Charakters):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.width = width

    def show_width(self):
        return self.width

class Snowman(Magical_Charakters):
    def __init__(self):
        super().__init__()

    def make_noise(self):
        noise = "Merry Christmas :)"
        return(noise)

    def intruduce_yourself(self):
        print("I'm a Snowman")

class Christmass_tree(Item):
    def __init__(self, name, color, height):
        super().__init__(name, color)
        self.height = height

    def show_color(self):
        return self.color

class Santas_sledge(Item):
    def __init__(self, name, width, height):
        super().__init__(name, items)
        self.width = width
        self.height = height

    def add_sledge(self):
        self.items.append(sledge)





