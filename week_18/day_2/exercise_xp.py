# Exercise 1 : Hello World 
    # Print the following output in one line of code: 
print("Hello World\n"*4) 
 
 
# Exercise 2 : Some Math 
    # Write code that calculates the result of: (99^3)*8  
    # (meaning 99 to the power of 3, times 8). 
print((99**3)*8) 
 
 
# Exercise 3 : What Is The Output ? 
    # Predict the output of the following code snippets: 
    # >>> 5 < 3                 False 
    # >>> 3 == 3                True  
    # >>> 3 == "3"              False 
    # >>> "3" > 3               False 
    # >>> "Hello" == "hello"    False 
 
 
#  Exercise 4 : Your Computer Brand 
    # Create a variable called computer_brand which value is  
    # the brand name of your computer. 
    # Using the computer_brand variable print a sentence  
    # that states the following: "I have a <computer_brand> computer". 
computer_brand = "Apple" 
print(F"I have an {computer_brand} computer ") 
 
 
#  Exercise 5 : Your Information 
    # Create a variable called name, and set it’s value to your name. 
    # Create a variable called age, and set it’s value to your age. 
    # Create a variable called shoe_size, and set it’s value to your shoe size. 
    # Create a variable called info and set it’s value to an interesting sentence about yourself.  
    # The sentence must contain all the variables created in parts 1, 2 and 3. 
    # Have your code print the info message. 
    # Run your code 
name,age,shoe_size = "George",31,43 
info = F"Hi! My name is {name}, I'm {age} years old. I wear shoes size {shoe_size}." 
print(info) 
 
 
#  Exercise 6 : A & B 
    # Create two variables, a and b. 
    # Each variable value should be a number. 
    # If a is bigger then b, have your code print Hello World. 
a=int(input("Enter number A: ")) 
b=int(input("Enter number B: ")) 
if a>b: 
    print("Hello world!") 
 
 
# Exercise 7 : Odd Or Even 
    # Write code that asks the user for a number and determines whether this number is odd or even. 
input_number = int(input("Please enter a number: ")) 
if input_number % 2 == 0: 
    print("Your number is even") 
else : print("Your number is odd") 
 
 
 
# Exercise 8 : What’s Your Name ? 
    # Write code that asks the user for their name and determines whether or not  
    # you have the same name, print out a funny message based on the outcome. 
users_name = input("What's your name?").lower() 
if users_name == "george": 
    print("Wow! We have the same names!") 
 
 
 
# Exercise 9 : Tall Enough To Ride A Roller Coaster 
    # Write code that will ask the user for their height in inches. 
    # If they are over 145cm print a message that states they are tall enough to ride. 
    # If they are not tall enough print a message that says they need to grow some more to ride. 
users_height_inches = int(input("How high are you in inches?")) 
users_height_cm = users_height_inches*2.54 
if users_height_cm > 145: 
    print(F"You're {users_height_cm}cm. That's tall enough to ride!") 
else: print(F"Sorry, you're only {users_height_cm}. You need to grow up!")