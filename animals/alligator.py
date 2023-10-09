from .animal import Animal
from movements import Swimming
class Alligator(Animal, Swimming):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} needs to eat a full {self.food} while "American Psycho" plays at full volume.')