#  Exercise 1 : Set 
    # Create a set called my_fav_numbers with all your favorites numbers. 
my_fav_numbers ={12,13,54,22} 
    # Add two new numbers to the set. 
my_fav_numbers.add(43) 
my_fav_numbers.add(42) 
 
    # Remove the last number. 
my_fav_numbers.remove(42) 
        # PERSONAL COMMENT:            
            # There's no sequence in sets, What's supposed to be the last number? the last added? 
 
 
    # Create a set called friend_fav_numbers with your friend’s favorites numbers. 
friend_fav_numbers={32,6,66,99,100} 
    # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers. 
our_fav_numbers= friend_fav_numbers.union(my_fav_numbers) 
# print(my_fav_numbers) 
print(our_fav_numbers) 
 
 
 
# Exercise 2: Tuple 
#     Given a tuple which value is integers, is it possible to add more integers to the tuple? 
# ANSWER:No, it's not possible 
 
 
 
# Exercise 3: List 
    # Using this list  
basket = ["Banana", "Apples", "Oranges", "Blueberries"] 
    # Remove “Banana” from the list. 
basket.remove("Banana") 
print(basket) 
    # Remove “Blueberries” from the list. 
basket.pop() 
print(basket) 
    # Add “Kiwi” to the end of the list. 
basket.append("Kiwi") 
print(basket) 
    # Add “Apples” to the beginning of the list. 
basket.insert(0,"Apples") 
print(basket) 
    # Count how many apples are in the basket. 
print(basket.count("Apples")) 
print(basket) 
    # Empty the basket. 
basket.clear() 
print(basket) 
 
 
 
 
# Exercise 4: Floats 
    # Recap – What is a float? What is the difference between an integer and a float? 
    # Can you think of another way to generate a sequence of floats? 
    # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5  
    # (don’t hard-code the sequence). 
float_sequence=[] 
my_float=1.5 
while my_float <=5: 
    if(my_float == int(my_float)): 
        float_sequence.append(int(my_float)) 
    else: 
        float_sequence.append(my_float) 
    my_float+=0.5 
print(float_sequence) 
 
 
 
 
# Exercise 5: For Loop 
    # Use a for loop to print all numbers from 1 to 20, inclusive. 
    # Using a for loop, that loops from 1 to 20(inclusive), print out every  
    # element which has an even index.   
for i in range(20): 
    if i % 2 == 0: 
        print(i+1)    #If I got it correctly - we don't care about the actual nuber we're printing 
                      # but only about it's index in a list [1,...,20] 
 
 
# Exercise 6 : While Loop 
    # Write a while loop that will continuously ask the user for their name,  
    # unless the input is equal to your name. 
user_name = "" 
# while user_name !="George": 
#     user_name=input("Guess my name!") 
print("You've guessed! YAY!") 
 
 
#  Exercise 7: Favorite Fruits 
    # Ask the user to input their favorite fruit(s) (one or several fruits). 
    # Hint : Use the built in input method. Ask the user to separate the fruits with a single space,  
    # eg. "apple mango cherry". 
    # Store the favorite fruit(s) in a list (convert the string of words into a list of words). 
    # Now that we have a list of fruits, ask the user to input a name of any fruit. 
    # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits!  
    # Enjoy!”. 
    # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”. 
user_fruits = input("Please write fruit separated with a space: ") 
user_list = user_fruits.split(" ") 
print(user_list) 
user_new_fruit = input("Select a fruit!") 
if user_new_fruit in user_list: 
    print("You chose one of your favorite fruits! Enjoy!") 
else: print("You chose a new fruit. I hope you enjoy") 
 
 
# Exercise 8: Who Ordered A Pizza ? 
    # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’  
    # stop asking for toppings. 
    # As they enter each topping, print a message saying you’ll add that topping to their pizza. 
    # Upon exiting the loop print all the toppings on the pizza pie and  
    # what the total price is (10 + 2.5 for each
    # topping). 
 
topping_total_price = 0 
ONE_TOPPING = 2.5 
toppings_list = [] 
select_topping="" 
while True: 
    select_topping=input("plese select a topping!") 
    if select_topping=="quit": break 
    toppings_list.append(select_topping) 
    topping_total_price+= ONE_TOPPING 
print(F"You've selected {', '.join(toppings_list)}. The total price is: {10+topping_total_price}$") 
 
 
 
# Exercise 9: Cinemax 
    # A movie theater charges different ticket prices depending on a person’s age. 
    # if a person is under the age of 3, the ticket is free. 
BABY_PRICE=0 
    # if they are between 3 and 12, the ticket is $10. 
KID_PRICE=10 
    # if they are over the age of 12, the ticket is $15. 
NORMAL_PRICE = 15 
    # Ask a family the age of each person who wants a ticket. 
family_size = int(input("How many people?")) 
total_cost=0 
for i in range(family_size): 
    age=int(input(F"Person {i+1}, how old are you?")) 
    if age <=3 : total_cost+= BABY_PRICE  #Normally doesn't matter, but what is prices change later? 
    elif age<=12 : total_cost+=KID_PRICE 
    else: total_cost+=NORMAL_PRICE 
print(F"You'r total would be: {total_cost}$") 
 
 
# A group of teenagers are coming to your movie theater and want to watch a movie that is  
# restricted for people between the ages of 16 and 21. 
# Given a list of names, write a program that asks teenager for their age,  
# if they are not permitted to watch the movie, remove them from the list. 
# At the end, print the final list. 
 
teens_names = ["Garry", "Nick", "Toby", "Andrew", "Belzebub", "Harry Potter"] 
for name in teens_names: 
    age_check = int(input(F"{name}, how old are you?")) 
    if age_check> 21 or age_check<16: 
        teens_names.remove(name) 
        print(F"Sorry, {name}, you can't go") 
print(F"Only {', '.join(teens_names)} can see the movie. Have fun!")