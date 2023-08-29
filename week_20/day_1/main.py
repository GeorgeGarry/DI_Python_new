# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# ## create an instance of the class
# p = Point(3,4)

# ## access the attributes
# print("p.x is:", p.x)
# print("p.y is:", p.y)


class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

first_person = Person("John", 36)
first_person.show_details()


class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")


class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

my_acount = BankAccount(12345, 1000)
my_acount.deposit(250)
my_acount.deposit(250)
my_acount.withdraw(400)
my_acount.withdraw(10000)
my_acount.view_balance()
my_acount.view_transactions()



# Try to recreate the class explained below:
# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.
# We can create a class called BlockedDoor that inherits from the base class Door.
# We just override the parent class's functions of open_door() and close_door() 
# with our own BlockedDoor version of those functions, which simply raises an Error that a 
# blocked door cannot be opened or closed.


class Door():
    def __init__(self, is_opened=True):
        self.is_opened=is_opened
    
    def open_door(self):
        self.is_opened=True
    # def close_door():
    #     self.is_opened=False



# class Blocked_door(Door):
#     def open_door():
#         print("Door is blocked")
#     def close_door():
#         print("Door is blocked")

my_door = Door()
my_door.open_door()