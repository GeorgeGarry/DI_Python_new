# Given this list:
list1 = [5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, 
# replace it with 200. Only update the first occurrence of a value

if 20 in list1:
    list1[list1.index(20)] = 200
    pass
else: print("sdfdfaf")
a_tuple = (10, 20, 30, 40)
a,b,c,d = a_tuple
print(a)
print(b)
print(c)
print(d)

user_number = int(input("enter a number "))
for num in range(1,10):
    print(F"{user_number} * {num} = ", user_number*num)
    pass

for num_1 in range(1,10):
    for num_2 in range(1,10):
        print(F"{num_1} * {num_2} = ", num_1*num_2)
        pass
    pass

num=0
while num <= 11:
    print(num)
    num+=1
