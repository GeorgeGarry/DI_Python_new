user_number = int(input())

if user_number%15 == 0:
    print("FizzBuzz")
elif user_number%3 == 0:
    print("Fizz")
elif user_number%5 == 0: 
    print("Buzz")
print("Finished")