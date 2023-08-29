# Challenge 1 
    # Ask the user for a number and a length. 
    # Create a program that prints a list of multiples of the number until the list length  
    # reaches length. 
 
# user_number = int(input("Give a number: ")) 
# user_length = int(input("Give length: ")) 
# numbers_list=[] 
# for i in range(user_length): 
#     numbers_list.append(user_number*(i+1)) 
# print(numbers_list) 
 
 
# Challenge 2 
    # Write a program that asks a string to the user,  
    # and display a new string with any duplicate consecutive letters removed. 
user_string = input("Please enter a word") 
user_string=user_string.replace(" ", "") 
user_string = user_string+ " " 
edited_string = user_string[0] 
print(edited_string) 
for i in range (len(user_string)-1): 
    if user_string[i] != user_string[i+1]: 
        edited_string = edited_string + user_string[i+1] 
edited_string = edited_string.replace(" ", "") 
print(edited_string)