# Exercise 1: Cats
    # Instructions
        # Using this class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

        # Instantiate three Cat objects using the code provided above.
        # Outside of the class, create a function that finds the oldest cat and returns the cat.
        # Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”.
        # Use the function previously created.
zoe = Cat("Zoe", 2)
kitty = Cat("Kitty", 5)
kel_thuzad= Cat("Kel'Thuzad", 300000)

all_cats_list = [zoe,kitty,kel_thuzad]

def find_the_oldest_cat(cats_list):
    oldest_cat = cats_list[0]
    for cat in cats_list:
        if cat.age > oldest_cat.age :
            oldest_cat = cat
    return oldest_cat
    # print(oldest_cat)

the_oldest_cat = find_the_oldest_cat(all_cats_list)
print(F"The oldest cat is {the_oldest_cat.name}, and is {the_oldest_cat.age} years old.")




# Exercise 2 : Dogs
    # Instructions

        # Create a class called Dog.
        # In this class, create an __init__ method that takes two parameters : name and height. 
        # This function instantiates two attributes, which values are the parameters.
        # Create a method called bark that prints the following string “<dog_name> goes woof!”.
        # Create a method called jump that prints the following string “<dog_name> 
        # jumps <x> cm high!”. x is the height*2.
        # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” 
        # and his height is 50cm.
        # Print the details of his dog (ie. name and height) and call the methods bark and jump.
        # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
        # Print the details of her dog (ie. name and height) and call the methods bark and jump.
        # Create an if statement outside of the class to check which dog is bigger.
        #  Print the name of the bigger dog.
class Dog():
    def __init__(self,name,height):
        self.name = name
        self.height = height
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print(F"{self.name} goes woof!")
# Create a method called jump that prints the following string “<dog_name> 
# jumps <x> cm high!”. x is the height*2.
    def jump(self):
        print(F"{self.name} jumps {self.height*2}cm high!")


davids_dog = Dog("Rex", 50)
print(F"David's dog is {davids_dog.name} and it's {davids_dog.height}cm high")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(F"Sarahs's dog is {sarahs_dog.name} and it's {sarahs_dog.height}cm high")
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height > sarahs_dog.height:
    print(F"{davids_dog.name} is bigger!")
else:
    print(F"{sarahs_dog.name} is bigger!")




# Exercise 3 : Who’s The Song Producer?
# Instructions

    # Define a class called Song, it will show the lyrics of a song.
    # Its __init__() method should have two arguments: self and lyrics (a list).
    # Inside your class create a method called sing_me_a_song that prints each element of lyrics 
    # on its own line.
    # Create an object, for example:

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



# Exercise 4 : Afternoon At The Zoo
    # Instructions

    # Create a class called Zoo.
    # In this class create a method __init__ that takes one parameter: zoo_name.
    # It instantiates two attributes: animals (an empty list) and name (name of the zoo).
    # Create a method called add_animal that takes one parameter new_animal. 
    # This method adds the new_animal to the animals list as long as it isn’t already in the list.
    # Create a method called get_animals that prints all the animals of the zoo.
    # Create a method called sell_animal that takes one parameter animal_sold. 
    # This method removes the animal from the list and of course the animal needs to exist in the list.
    # Create a method called sort_animals that sorts the animals alphabetically and groups them together
    # based on their first letter. 

class Zoo():
    def __init__(self, zoo_name, animals=[]):
        self.zoo_name=zoo_name
        self.animals=animals
    
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(F"we already have  {new_animal} in the {self.zoo_name}")
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(F"We don't have {animal_sold} in the {self.zoo_name}")

    def get_animals(self):
        print(self.animals)

    def sort_animals(self):
        print(self.animals.sort())

my_zoo = Zoo("new_zoo")
my_zoo.add_animal("lion")
my_zoo.add_animal("pig")
my_zoo.add_animal("elephant")
my_zoo.sell_animal("zebra")
my_zoo.sell_animal("zebra")
my_zoo.get_animals()
my_zoo.sort_animals()