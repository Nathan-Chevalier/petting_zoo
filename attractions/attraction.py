class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def report(self):
        print(f'{self.attraction_name} is {self.description}.  You can find the following animals here:')
        for animal in self.animals:
            print(f'\t* {animal.name} the {animal.species}')

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'
    
    def __len__(self):
        return len(self.animals)
    
    @property
    def last_critter_added(self):
        return f'{self.animals[-1]} is our newest addition!'