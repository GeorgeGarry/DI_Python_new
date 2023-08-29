# Daily Challenge: Old MacDonald’s Farm

# Take a look at the following code and output:
    # Create a class called Farm. How should it be implemented?
    # Does the Farm class need an __init__ method? If so, what parameters should it take?
    # How many methods does the Farm class need?
    # Do you notice anything interesting about the way we are calling the add_animal method? 
    # What parameters should this function have? How many…?
    # Test your code and make sure you get the same results as the example above.
    # Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

class Farm:
    animals = {}
    def __init__(self, farm_name):
        self.farm_name = farm_name
    def add_animal(self, animal, qtty=1):
        if animal in self.animals.keys():
            self.animals[animal] += qtty
        else:
            self.animals[animal] = qtty
    def get_info(self):
        res_str = ""
        for i in self.animals:
            res_str += F"{i} : {self.animals[i]}\n"
        res_str += "   E-I-E-I-0!"
        return res_str
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))
    def get_short_info(self):
        animals_arr = self.get_animal_types()
        info_str = "McDonald’s farm has"
        for i in range(len(animals_arr)):
            if (i == len(animals_arr)-1):
                info_str += F" and {animals_arr[i]}."
            else:
                info_str += F" {animals_arr[i]}s,"
        return info_str




macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())


# Add a method called get_animal_types to the Farm class. 
# This method should return a sorted list of all the animal types (names) in the farm.
# With the example above, the list should be: ['cow', 'goat', 'sheep'].

print(macdonald.get_animal_types())

# Add another method to the Farm class called get_short_info. 
# This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. 
# The method should call the get_animal_types function to get a list of the animal
print(macdonald.get_short_info())