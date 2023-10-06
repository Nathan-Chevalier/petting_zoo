from datetime import date

#? Walking Class animals










#? Swimming class animals











#? Slithering Class Animals







class LeglessLizard:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

class CornSnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

stanley = Alligator("Stanley", "Florida Alligator")
mr_ouchie = Rattlesnake("Mr. Ouchie", "Common Rattlesnake")
dunkey = Donkey("Dunkey", "Donkey")

