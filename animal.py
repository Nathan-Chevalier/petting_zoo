class Animal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num

    def feed(self):
        feed_message = f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
        print(feed_message)
        return feed_message