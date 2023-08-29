# Part 1 : Quizz :

# Answer the following questions

# What is a class?   
    # It's a template (instruction or blueprint) for creating objects
# What is an instance?
    # It is an object created from some class (according to that template)
# What is encapsulation?
    # 
# What is abstraction?
    # It is a process of simplifying big complex code by breaking it down to smaller parts
    # I think mostly you can experience that by using functions or classes and its' methods
# What is inheritance?
    # It is an ability of an instance object to inherit some attributes and/or methods of a parent class
# What is multiple inheritance?
    # Same as previous but in this case an object can iherit from multiple classes at the same time
# What is polymorphism?
    # I think it is a way for a multy-inherit instance to be used easier by overriding some methods and/or attributes
# What is method resolution order or MRO?
    # It's a sequence of the way methods are inherited and called




# Part 2: Create A Deck Of Cards Class.

# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value 
# (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then 
# rearranges them randomly.
# should have a method called deal which deals a single card from the deck. 
# After a card is dealt, it should be removed from the deck.


class Card():
    cards = {}