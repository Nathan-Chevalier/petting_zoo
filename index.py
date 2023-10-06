from datetime import date

from slithering import BurmesePython, Copperhead, CornSnake, LeglessLizard, Rattlesnake
from swimming import Alligator, Axolotl, Carp, Crocodile, SeaSnake
from walking import Alpaca, Donkey, Goat, Llama, Monkey


roberto = Alpaca("Roberto", "alpaca", "midday")

print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
