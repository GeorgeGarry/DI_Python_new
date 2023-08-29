import game

results = {
    "win": 0,
    "loss": 0,
    "draw": 0
    }

def print_results(results):
    print("Victories: ", results["win"])
    print("Losses: ", results["loss"])
    print("Dwars: ", results["draw"])

def edit_results(results,key):
    results[key]+=1

def get_user_menu_choice():
    user_choice_valid = False
    while not user_choice_valid:
        try:
            user_menu_choice = int(input("""
            Press 1 - Play a new game
            Press 2 - Show scores 
            Press 3 - Quit
            Your choice: """))
        except: 
            print("incorrect input. input only a number")
            continue

        if user_menu_choice == 1:
            user_choice_valid = True
            return {"message":"New game:", "code": 1}
        elif user_menu_choice == 2:
            user_choice_valid = True
            return {"message":"Score is:", "code": 2}
        elif user_menu_choice == 3:
            user_choice_valid = True
            return {"message":"See you soon! bye", "code": 3}
        else: print("incorrect input. please input 1, 2 or 3")

def main():
    session_finished = False
    while not session_finished:
        select_menu = get_user_menu_choice()
        print(select_menu["message"])
        if select_menu["code"] == 1:
            new_game = game.Game()
            one_game_result = new_game.play()
            edit_results(results,one_game_result["code"])
            print(one_game_result["message"])
            pass
        elif select_menu["code"] == 2:
            print_results(results)
        elif select_menu["code"] == 3:
            session_finished = True

main()
