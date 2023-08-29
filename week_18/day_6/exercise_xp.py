#  Exercise 1 : Convert Lists Into Dictionaries 
    # Instructions 
    # Convert the two following lists, into dictionaries. 
    # Hint: Use the zip method 
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30] 
my_dict =dict(zip(keys,values)) 
print(my_dict) 
 
 
 
#  Exercise 2 : Cinemax 
    # Instructions 
    # A movie theater charges different ticket prices depending on a person’s age. 
    # if a person is under the age of 3, the ticket is free. 
BABY_PRICE=0 
    # if they are between 3 and 12, the ticket is $10. 
KID_PRICE=10 
    # if they are over the age of 12, the ticket is $15. 
NORMAL_PRICE = 15 
 
    # Given the following object: 
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8} 
    # How much does each family member have to pay ? 
    # Print out the family’s total cost for the movies. 
total_cost=0 
for key in family: 
    if family[key] < 3: 
        print(F"{key} has to pay {BABY_PRICE}$") 
        total_cost+=BABY_PRICE 
    elif family[key] <= 12: 
        print(F"{key} has to pay {KID_PRICE}$") 
        total_cost+=KID_PRICE 
    else: 
        print(F"{key} has to pay {NORMAL_PRICE}$") 
        total_cost+=NORMAL_PRICE 
 
print(F"The total would be {total_cost}$") 
 
 
 
# Exercise 3: Zara 
    # Here is some information about a brand    
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values). 
brand={ 
    "name": "Zara",  
    "creation_date": 1975, 
    "creator_name": "Amancio Ortega Gaona ", 
    "type_of_clothes": ["men", "women", "children", "home" ], 
    "international_competitors":[ "Gap", "H&M", "Benetton" ], 
    "number_stores": 7000 , 
    "major_color":{  
        "France": "blue",  
        "Spain": "red",  
        "US": ["pink", "green"]} 
} 
# 3. Change the number of stores to 2. 
brand["number_stores"]=2 
# 4. Print a sentence that explains who Zaras clients are. 
clients=brand["type_of_clothes"][0:3] 
print(F"Our clients are {', '.join(clients)}") 
# 5. Add a key called country_creation with a value of Spain. 
brand["country_creation"]="Spain" 
print(brand) 
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual. 
brand.get("international_competitors").append("Desigual") 
print(brand["international_competitors"]) 
# 7. Delete the information about the date of creation. 
del brand["creation_date"] 
print(brand) 
# 8. Print the last international competitor. 
print(brand["international_competitors"][-1]) 
# 9. Print the major clothes colors in the US. 
print(brand["major_color"]["US"]) 
# 10. Print the amount of key value pairs (ie. length of the dictionary). 
print(list(zip(brand))) 
# 11. Print the keys of the dictionary. 
print(brand.keys()) 
# 12. Create another dictionary called more_on_zara with the following details: 
more_on_zara={ 
    "creation_date": 1975, 
    "number_stores": 10000 
} 
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand. 
# 14. Print the value of the key number_stores. What just happened ? 
brand.update(more_on_zara) 
print(brand["number_stores"]) 
 
 
 
 
 
 
# Exercise 4 : Disney Characters 
    # Instructions 
    # Use this list : 
users = ["Mickey","Minnie","Donald","Ariel","Pluto"] 
 
    # Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers. 
    # Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers. 
    # Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically. 
    # Only recreate the 1st result for: 
    # The characters, which names contain the letter “i”. 
    # The characters, which names start with the letter “m” or “p”. 
disney_users_A={} 
disney_users_B={} 
disney_users_C={} 
users_sort=sorted(users) 
for i in range(len(users)): 
    disney_users_A[users[i]]=i 
    disney_users_B[i]=users[i] 
    disney_users_C[users_sort[i]]=i 
 
#1/ 
print(disney_users_A) 
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4} 
 
#2/ 
 
print(disney_users_B) 
{0: "Mickey",1: "Minnie",2: "Donald", 3: "Ariel", 4: "Pluto"} 
 
#3/  
 
print(disney_users_C) 
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
