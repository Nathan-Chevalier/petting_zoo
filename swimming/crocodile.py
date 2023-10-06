from datetime import date
class Crocodile:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
        feed_message = f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
        print(feed_message)
        return feed_message