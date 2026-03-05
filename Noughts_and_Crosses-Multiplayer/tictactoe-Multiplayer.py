# TicTacToe Game
print("Welcome to TICTACTOE")

# Setting an object, board, to represent the 3 x 3 grid
board = [" "] * 9

# Function to print the full board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# This calls the print board function
print_board(board)

# Function to request and process Player 1's moves
def player1():
    try:
        move = int(input("Player 1, enter your move (1-9): "))
        if move < 1 or move > 9:
            raise ValueError
        elif board[move - 1] == " ":
            board[move - 1] = "X"
        else:
            print("Invalid move. Try again.")
            player1()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9")
        player1()

# Function to request and process Player 2's moves
def player2():
    try:
        move = int(input("Player 2, enter your move (1-9): "))
        if move < 1 or move > 9:
            raise ValueError
        elif board[move - 1] == " ":
            board[move - 1] = "O"
        else:
            print("Invalid move. Try again.")
            player2()
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9")
        player2()

# Function to check if Player 1 has won.
def check_win_1():
    #check_for_draw()
    is_winner_1 = False
    for n in range (0, 3): # combinations (0,3,6) (1,4,7) and  (2,5,8). ALL VERTICAL COMBINATIONS
        if board [n] == board [n + 3] == board [n + 6] == "X":  
            print("Player 1 wins")
            is_winner_1 = True
            # CLI decoration and requesting input so programm stays open until user hits ENTER
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    for n in (0, 3, 6): # combinations (0,1,2) (3,4,5) (6,7,8). ALL HORIZONTAL COMBINATIONS
        if board [n] == board [n + 1] == board [n + 2] == "X":  
            print("Player 1 wins")
            is_winner_1 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    for n in [0]: # combinations (0, 4, 8) DIAGONAL LEFT TO RIGHT
        if board [n] == board [n + 4] == board [n + 8] == "X":  
            print("Player 1 wins")
            is_winner_1 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    for n in [2]: # combinations (2,4,6) DIAGONAL RIGHT TO LEFT
        if board [n] == board [n + 2] == board [n + 4] == "X":  
            print("Player 1 wins")
            is_winner_1 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    # Checking for draw below. if there is a draw, the programme terminates based on the function.
    check_for_draw()
    if not is_winner_1:
        gameplay_2()

# Function to check if Player 2 has won.
def check_win_2():
    #check_for_draw()
    is_winner_2 = False
    for n in range (0, 3): # combinations (0,3,6) (1,4,7) and  (2,5,8). ALL VERTICAL COMBINATIONS
        if board [n] == board [n + 3] == board [n + 6]== "O":  
            print("Player 2 wins")
            is_winner_2 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()
          
    for n in (0, 3, 6): # combinations (0,1,2) (3,4,5) (6,7,8). ALL HORIZONTAL COMBINATIONS
        if board [n] == board [n + 1] == board [n + 2] == "O":  
            print("Player 2 wins")
            is_winner_2 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    for n in [0]: # combinations (0, 4, 8) DIAGONAL LEFT TO RIGHT
        if board [n] == board [n + 4] == board [n + 8] == "O":  
            print("Player 2 wins")
            is_winner_1 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    for n in [2]: # combinations (2,4,6) DIAGONAL RIGHT TO LEFT
        if board [n] == board [n + 2] == board [n + 4] == "O":  
            print("Player 1 wins")
            is_winner_1 = True
            # CLI decoration
            decoration()
            stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
            exit()

    # Checking for draw below. if there is a draw, the programme terminates based on the function.
    check_for_draw()
    if not is_winner_2:
        gameplay_1()

# Function to check for a draw. Called within the check_win function
def check_for_draw():
    if all (n in ["X", "O"] for n in board):
        print("It's a Draw!")
        decoration()
        stayopen = input(("*" *(18)) + ("GAME OVER") + ("*")*(18))
        exit()

# Composite function to process Player 1's turns
def gameplay_1():
        player1()
        print_board(board)
        # Check if Player 1 has won
        check_win_1()

# Composite function to process Player 2's turns.
def gameplay_2():
        player2()
        print_board(board)
        # Check if Player 2 has won
        check_win_2()

# CLI decoration with asterisks
def decoration():
    import time
    for i in range(1,20, 2):
        j = 20 - i
        print(("*" *(i)) + ((" ")*(45-(2*i))) + ("*")*(i))
        time.sleep(0.2)

# Starting the game by calling player 1's gameplay function
gameplay_1()


