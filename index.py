from datetime import date

from slithering import BurmesePython, Copperhead, CornSnake, LeglessLizard, Rattlesnake
from swimming import Alligator, Axolotl, Carp, Crocodile, SeaSnake
from walking import Alpaca, Donkey, Goat, Llama, Monkey
from attractions import PettingZoo, Wetlands, SnakePit


gary = Llama("Gary", "llama", "Swing", "Llama Food", 89)
bobby = SeaSnake("Bobby", "Sea Snake", "Fish", 27)
ricky = Rattlesnake("Ricky", "Rattlesnake", "Mice", 224)
alex = Alligator("Alex", "Alligator", "Person", 81767)
varmint_village = PettingZoo("Varmint Village", "a really bad idea")

gary.feed()
bobby.feed()
ricky.feed()
alex.feed()
print(gary)
print(bobby)
print(ricky)
varmint_village.add(gary)
varmint_village.report()
print(varmint_village.last_critter_added)

