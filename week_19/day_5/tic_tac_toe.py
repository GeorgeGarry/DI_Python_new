a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3 = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

grid=[
    a_1, a_2, a_3,
    b_1, b_2, b_3,
    c_1, c_2, c_3
]

field = F"""
        ****************
        *  {a_1} | {a_2} | {a_3}   *
        * ---|---|---  *
        *  {b_1} | {b_2} | {b_3}   *
        * ---|---|---  *
        *  {c_1} | {c_2} | {c_3}   *
        ****************
        """

track_moves={
    "X":[],
    "O":[]
}


win_combinations = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
]


game_not_finished = True
player="X"
turns=0


def player_move():
    global turns
    global field
    global player
    global game_not_finished
    print(field)
    move_is_not_done=True
    while move_is_not_done:
        
        try:
            move = int(input(F"Player {player}, please choose a spot to move: "))
        except: 
            print("Please input a number")
            continue
        if move<1 or move>9:
            print("Please choose only a number 1-9")
            continue
        if check_if_move_legal(move):
            print("move is legal")
            grid[move-1] = player
            a_1, a_2, a_3, b_1, b_2, b_3, c_1, c_2, c_3 = grid
            field = F"""
                ****************
                *  {a_1} | {a_2} | {a_3}   *
                * ---|---|---  *
                *  {b_1} | {b_2} | {b_3}   *
                * ---|---|---  *
                *  {c_1} | {c_2} | {c_3}   *
                ****************
                """
            track_moves[F"{player}"].append(move)
        else:
            print("Sorry, this spot is already taken. Try another one")
            continue
        
        print("Great choice!")
        print("*" * 100)
        turns+=1
        move_is_not_done=False

    check_win(player)
    switch_players()


        
def check_win(player):
    global game_not_finished
    global turns
    if turns >= 9:
        print("Draw!")
        game_not_finished = False
        return True 
    for combination in win_combinations:
        if all(move in track_moves[player] for move in combination):
            print(F"Player {player} has won!!!")
            game_not_finished=False
            return True
    return False


def check_if_move_legal(move):
    if grid[move-1] == "X" or grid[move-1] == "O": 
        return False
    return True

def switch_players():
    global player
    if player =="X":
        player="O"
    else: 
        player="X"

        
def game():
    while game_not_finished:
        player_move()
    pass

game()
