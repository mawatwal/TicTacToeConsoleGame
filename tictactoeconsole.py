# global variables
game_still_going = True
game_winner = None
current_player = "X"

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

# definiton to display the board
def display_board():
    print("\n")
    print(board[0]+" "+ board[1]+" "+ board[2])
    print(board[3]+" "+ board[4]+" "+ board[5])
    print(board[6]+" "+ board[7]+" "+ board[8])
    print("\n")

def play_game():
    display_board()
    while game_still_going:
        player_turn(current_player)
        check_if_game_over()
        change_player()
    if game_winner == "X" or game_winner == "O":
        print(game_winner + " won")
    elif game_winner == None:
        print("It's a Tie.")

# definition to take input from player and put it in the board position
def player_turn(player):
    print(player + " 's turn.")
    position = input("Choose a position from 1 to 9: ")
    valid = False
    # to check whether the player has input the correct input in-bound
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position")
        # to convert input string into integer value and subtract 1 from the converted integer value
        position = int(position) - 1
        
        if board[position] == "_":
            valid = True
        else:    
            print("You can't go there. Go again.")
    
    board[position] = player
    display_board()
 
# definiton to check whether the game is over or not
def check_if_game_over():
    # game will be over by either a tie (in case none of the spaces are left in the board) or a win
    check_for_winner()
    check_if_tie()

# definition to check whether there is a winner
def check_for_winner():
    global game_winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        game_winner = row_winner
    elif column_winner: 
        game_winner = column_winner
    elif diagonal_winner:
        game_winner = diagonal_winner
    else:
        game_winner = None
    return

# definition to check whether the win is due to rows
def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
    return

# definition to check whether the win is due to columns
def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
    return

# definiton to check whether the win is due to diagonals
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None
    return

# definition to check if there is a tie
def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False
        return True
    else:
        return False

# definition to change the player / flip the player
def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

# call the main function for execution
play_game()
