from datetime import date

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
    
    def __str__(self):
        return f'{self.name} the {self.species}'
    
    @property #When chip_num is accessed, the private value set by __chip_number will display instead.  Property is a "Getter" function
    def chip_num(self):
        return self.__chip_number
    
    @chip_num.setter #Prevents the number from being set outside of initialization 
    def chip_num(self, num):
        pass