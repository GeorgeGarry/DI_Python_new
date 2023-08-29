import random 
# Daily Challenge: Build Up A String 
# Instructions 
    # Using the input function, ask the user for a string. The string must be 10 characters long. 
    # If it’s less than 10 characters, print a message which states “string not long enough”. 
    # If it’s more than 10 characters, print a message which states “string too long”. 
    # If it’s 10 characters, print a message which states “perfect string” and continue the exercise. 
while True: 
    user_string = input("Please input some text. should be 10 characters") 
    if len(user_string) > 10: 
        print("string too long") 
    elif len(user_string) < 10: 
        print("string not long enough") 
    else:  
        print("perfect string") 
        break 
    # Then, print the first and last characters of the given text. 
print(user_string[0], user_string[9]) 
    # Using a for loop, construct the string character by character: 
    # Print the first character, then the second, then the third, until the full string is printed. 
    # The user enters "HelloWorld" 
constructor_string = "" 
for i in user_string: 
    constructor_string += i 
    print(constructor_string) 
 
 
# 4. Bonus: Swap some characters around then print the newly jumbled string  
# (hint: look into the shuffle method). For example:   Hlrolelwod 
 
str_to_list = list(user_string.lower()) 
random.shuffle(str_to_list) 
random_str = "" 
for letter in str_to_list: 
    random_str += letter 
print(random_str.capitalize())
