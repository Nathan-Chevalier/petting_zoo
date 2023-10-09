from datetime import date

from animals import BurmesePython, Copperhead, CornSnake, LeglessLizard, Rattlesnake, Alligator, Axolotl, Carp, Crocodile, SeaSnake, Alpaca, Donkey, Goose, Llama, Monkey
from attractions import PettingZoo, Wetlands, SnakePit


gary = Llama("Gary", "llama", "Swing", "Llama Food", 89)
bobby = SeaSnake("Bobby", "Sea Snake", "Fish", 27)
ricky = Rattlesnake("Ricky", "Rattlesnake", "Mice", 224)
alex = Alligator("Alex", "Alligator", "Person", 81767)
greg = Goose("Greg", "Canada Goose", "Morning", "Food Pellets", 8009)
varmint_village = PettingZoo("Varmint Village", "a really bad idea")

gary.feed()
bobby.feed()
ricky.feed()
alex.feed()
greg.feed()
greg.swim()
greg.run()
print(gary)
print(bobby)
print(ricky)
varmint_village.add(gary)
varmint_village.report()
print(varmint_village.last_critter_added)

