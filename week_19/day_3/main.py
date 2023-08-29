from functools import reduce
# reduce(function, iterable[, initializer])


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
print(list(map(lambda name: F"Hello {name}", filter(lambda name: len(name)<= 4, people))))


my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
result_sum=0

for num in my_list:
        try:
            result_sum+=num
        except:
            continue
# print(result_sum)
# try:
#     print(reduce(lambda num_1, num_2: num_1 + num_2, my_list))
# except:
#     print("bad")



valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:    # TRY THIS
        userage    = int(userage)
    except: # IF YOU GOT AN ERROR
        print("Wrong age!")
    else:   # ELSE
        valid_flag = True

print("Next year, your age will be",userage+1)
# >>How old are you?3
# Next year, your age will be 4



x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was {x}'.format(x=x))
#The error that will appear is your own custom error
#Traceback (most recent call last):
  #File "pyblog/app.py", line 52, in <module>
    #raise Exception('x should not exceed 5. The value of x was {x}'.format(x=x))
#Exception: x should not exceed 5. The value of x was 10'

#Process finished with exit code 1

z = 9
try:
    assert 1 == z
except AssertionError:
    print("Error: Those are not equals")