import random

class Game():
    user_item = ""
    computer_item = ""
    options = ["rock", "paper", "scissors"]

    def __init__(self):
        pass

    def play(self):
        self.get_computer_item()
        self.get_user_item()
        return self.get_game_result()

    def get_user_item(self):
        user_choice_valid = False
        while not user_choice_valid:
            user_input = input("""
            Please choose your move:
                rock
                paper
                scissors
            """)
            if user_input in self.options:
                self.user_item = user_input
                user_choice_valid = True
            else :
                print("Incorrect input!")
            
    def get_computer_item(self):
        self.computer_item = self.options[random.randint(0, 2)]
        
    def get_game_result(self):
        if self.user_item == self.computer_item:
            return {"message":F"""
            You selected {self.user_item}
            Computer selected {self.computer_item}
            It's a tie!""", "code": "draw"}
        elif (
            (self.user_item == "rock" and self.computer_item == "scissors")
            or (self.user_item == "paper" and self.computer_item == "rock")
            or (self.user_item == "scissors" and self.computer_item == "paper")
        ):
            return {"message":F"""
            You selected {self.user_item}
            Computer selected {self.computer_item}
            You won! Congradulations!""", "code": "win"}

        return {"message":F"""
            You selected {self.user_item}
            Computer selected {self.computer_item}
            You lose! Better luck next time.""", "code": "loss"}
