from datetime import date

from animals import BurmesePython, Copperhead, CornSnake, LeglessLizard, Rattlesnake, Alligator, Axolotl, Carp, Crocodile, SeaSnake, Alpaca, Donkey, Goose, Llama, Monkey
from attractions import PettingZoo, Wetlands, SnakePit


gary = Llama("Gary", "llama", "Swing", "Llama Food", 89)
bobby = SeaSnake("Bobby", "Sea Snake", "Fish", 27)
ricky = Rattlesnake("Ricky", "Rattlesnake", "Mice", 224)
alex = Alligator("Alex", "Alligator", "Person", 81767)
greg = Goose("Greg", "Canada Goose", "Morning", "Food Pellets", 8009)
varmint_village = PettingZoo("Varmint Village", "a really bad idea")
snake_surplus = SnakePit("Snake Surplus", "a place that has a lot of snakes")
wet_williams = Wetlands("Wet Williams'", "very damp and very old")




varmint_village.add(gary)
snake_surplus.add(alex)
wet_williams.add(bobby)
varmint_village.report()
snake_surplus.report()
wet_williams.report()
print(varmint_village.last_critter_added)
print(varmint_village)

