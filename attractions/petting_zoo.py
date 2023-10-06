class PettingZoo:
    
    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def report(self):
        print(f'{self.attraction_name} is {self.description}.  You can find the following animals here:')
        for animal in self.animals:
            print(f'\t* {animal.name} the {animal.species}')

    @property
    def last_critter_added(self):
        return f'{self.animals[-1]} is our newest addition!'