from .animal import Animal
class Alligator(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} needs to eat a full {self.food} while "American Psycho" plays at full volume.')