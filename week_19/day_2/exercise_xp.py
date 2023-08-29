import random 
# Exercise 1 : What Are You Learning ? 
    # Instructions 
    # Write a function called display_message() that prints one sentence telling everyone what you are learning in this course. 
    # Call the function, and make sure the message displays correctly. 
 
def display_message(): 
    print("I'm learniing python functions.") 
 
display_message() 
 
 
# Exercise 2: What’s Your Favorite Book ? 
    # Instructions 
    # Write a function called favorite_book() that accepts one parameter called title. 
    # The function should print a message, such as "One of my favorite books is <title>". 
    # For example: “One of my favorite books is Alice in Wonderland” 
    # Call the function, make sure to include a book title as an argument when calling the function. 
 
def favorite_book(title="Necronomicon"): 
    print(F"One of my favorite books is {title}") 
 
favorite_book("The fellowship of the ring") 
 
 
 
# Exercise 3 : Some Geography 
    # Instructions 
    # Write a function called describe_city() that accepts the name of a city and its country  
    # as parameters. 
    # The function should print a simple sentence, such as "<city> is in <country>". 
    # For example “Reykjavik is in Iceland” 
    # Give the country parameter a default value. 
    # Call your function. 
 
def describe_city(city,country="Israel"): 
    print(F"{city} is in {country}") 
 
describe_city("Tel-Aviv") 
 
 
# Exercise 4 : Random 
    # Instructions 
    # Create a function that accepts a number between 1 and 100 and generates  
    # another number randomly between 1 and 100. 
    # Compare the two numbers, if it’s the same number, display a success message,  
    # otherwise show a fail message and display both numbers. 
 
def guess_1_100(user_num): 
    num=random.randrange(1,100) 
    if num == int(user_num): 
        print("YAY! You've guessed") 
    else: print(F"Sorry, your number is {user_num} and mine is {num}") 
 
guess_1_100(78) 
 
 
 
 
# Exercise 5 : Let’s Create Some Personalized Shirts ! 
    # Instructions 
    # Write a function called make_shirt() that accepts a size and the text of a message  
    # that should be printed on the shirt. 
    # The function should print a sentence summarizing the size of the shirt 
    # and the message printed on it, such as "The size of the shirt is <size> and the text is <text>" 
    # Call the function make_shirt(). 
 
    # Modify the make_shirt() function so that shirts are large by default with a message  
    # that reads “I love Python” by default. 
    # Make a large shirt with the default message 
    # Make medium shirt with the default message 
    # Make a shirt of any size with a different message. 
 
    # Bonus: Call the function make_shirt() using keyword arguments. 
 
def make_shirt(size="Large", text="I love Python!"): 
    print(F"The size of the shirt is '{size}' and the text is '{text}'") 
 
make_shirt() 
make_shirt(size="Medium") 
make_shirt(text="This is a T-shirt") 
 
 
# Exercise 6 : Magicians … 
    # Instructions 
    # Using this list of magician’s names.  
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel'] 
    # Pass the list to a function called show_magicians(), which prints the name of  
    # each magician in the list. 
    # Write a function called make_great() that modifies the list of magicians  
    # by adding the phrase "the Great" to each magician’s name. 
    # Call the function make_great(). 
    # Call the function show_magicians() to see that the list has actually been modified. 
 
def show_magicians(array): 
    for name in array: 
        print(name) 
 
def make_great(array): 
    for i in range(len(array)): 
        array[i] += " the Great!" 
 
make_great(magician_names) 
show_magicians(magician_names)