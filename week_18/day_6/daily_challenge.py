# Daily Challenge: Dictionaries 
    # Challenge 1 
    # Ask a user for a word 
    # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list. 
 
    # Make sure the letters are the keys. 
    # Make sure the letters are strings. 
    # Make sure the indexes are stored in a list and those lists are values. 
user_input=input("give a word: ") 
# user_input="dodo" 
my_dict={} 
for i in range(len(user_input)): 
    print(user_input[i]) 
    if my_dict.get(user_input[i]) == None: 
        my_dict[user_input[i]]=[] 
    my_dict[user_input[i]].append(i) 
print(my_dict) 
 
 
# Challenge 2 
    # Create a program that prints a list of the items you can afford in the store 
    # with the money you have in your wallet. 
    # Sort the list in alphabetical order. 
    # Return “Nothing” if you can’t afford anything from the store. 
     
items_purchase = { 
  "Water": "$1", 
  "Bread": "$3", 
  "TV": "$1,000", 
  "Fertilizer": "$20" 
} 
wallet = "$300" 
 
""" 
# to test the "Nothing" feature 
items_purchase = { 
  "Phone": "$999", 
  "Speakers": "$300", 
  "Laptop": "$5,000", 
  "PC": "$1200" 
} 
wallet = "$1"  
""" 
 
money = int(wallet.replace("$","")) 
can_afford=[] 
can_afford_nothing=True 
for key in items_purchase: 
    price=int(items_purchase[key].replace("$","").replace(",","")) 
    if money>=price: 
        can_afford_nothing=False 
        can_afford.append(key) 
 
if can_afford_nothing: 
    can_afford = "Nothing" 
print(can_afford)