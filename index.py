from datetime import date

from slithering import BurmesePython, Copperhead, CornSnake, LeglessLizard, Rattlesnake
from swimming import Alligator, Axolotl, Carp, Crocodile, SeaSnake
from walking import Alpaca, Donkey, Goat, Llama, Monkey
from attractions import PettingZoo, Wetlands, SnakePit


roberto = Alpaca("Roberto", "alpaca", "midday", "Alpaca Chow")
gary = Llama("Gary", "llama", "Swing", "Llama Food")
varmint_village = PettingZoo("Varmint Village", "a really bad idea")

print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
gary.feed()
roberto.feed()
print(roberto)
print(gary)
varmint_village.add(roberto)
varmint_village.add(gary)
varmint_village.report()