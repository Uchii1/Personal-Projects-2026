# A Tic-Tac-Toe (Noughts and Crosses) game between a human player (Player) and the computer programme (Computer). 

# Importing required modules
import random
import os
import time
import pyfiglet # For decorativ lettering

# A decorative sequence
def decorative_sequence():
    for i in range(12):
        print(("*" *(i)), end=" ", flush = True)       
        time.sleep(0.1)

# Running the decorative sequence at the start of the programme
decorative_sequence()
print(" \n            WELCOME TO TIC TAC TOE                ")
decorative_sequence()
time.sleep(0.5)

# General screen clearing that clears the whole screen
def screen_clearing():
    os.system('cls' if os.name == 'nt' else 'clear')

# Minor screen clearing that leaves a sticky title
def minor_clear_screen(sticky = ""):
    print("\033[2J\033[H", end="")
    os.system('cls' if os.name == 'nt' else 'clear')  
    # This is printed if no argument 'sticky' is passed.
    if not sticky:
        print(pyfiglet.figlet_format("TIC TAC TOE", font="slant"))


# The Programme's main function: game_play()
def game_play():

    # Defining relevant functions and data objects for the main programme function

    # A list to store all boxes
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # A list to store boxes no one has played in
    unplayed_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # A list to store the boxes the player has played in
    player_spaces =[]
   
   # Clearing the screen, leaving the title on the display
    minor_clear_screen()

    # Defining and calling a function to check if the user wants to play again
    def play_again():
        choice = input("\n \nWould you like to play again? \n[1] Yes \n[2] No \nYour Choice: ")
        choice = int(choice)
        if choice == 1:
            minor_clear_screen()
            game_play()
        else:
            confirm = input("\n \nAre you sure you want to leave? \n[1] No, Play again \n[2] Yes, I want to leave. \nYour Choice: ")
            confirm = int(confirm)
            if confirm == 1:
                minor_clear_screen()
                game_play()
            else:
                print("Thanks for playing! Hit ENTER to Exit")
                exit()

    # This function will print the whole board. 
    def print_board(board):
        print("\n")
        print(f"              {board[0]} | {board[1]} | {board[2]}")
        print("              --+---+--")
        print(f"              {board[3]} | {board[4]} | {board[5]}")
        print("              --+---+--")
        print(f"              {board[6]} | {board[7]} | {board[8]}")
        print(" ")  # Blank line for neatness

    # Calling the print_board() function
    print_board(board)

    # This function will give an impression of loading
    def loading_dots():
        print(" ")  # Blank line for neatness
        print("Computer Playing", end = " ")
        for i in range(3):
            print(".", end= "", flush = True)  # The flush keyword ensures the dots are printed at each iteration of the loop
            time.sleep(0.5) # There are 0.5 seconds between the dots being displayed.
        # The below will clear the screen for the next function to run
        minor_clear_screen()

    # Function for a simple CLI decoration
    def decoration():
        for i in range(1,10, 2):
            j = 10 - i
            print(("*" *(i)) + ((" ")*(45-(2*i))) + ("*")*(i))
            time.sleep(0.25)
        print(" ")
            
    # Function to check if Player 1 has won.
    def check_win_1():
        for n in range (0, 3): # Combinations (0,3,6) (1,4,7) and  (2,5,8). ALL VERTICAL COMBINATIONS
            if board [n] == board [n + 3] == board [n + 6] == "X":
                print_board(board)  
                print("           Player 1 wins           ")
                # CLI decoration and requesting input so programm stays open until user hits ENTER
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()

        for n in (0, 3, 6): # Combinations (0,1,2) (3,4,5) (6,7,8). ALL HORIZONTAL COMBINATIONS
            if board [n] == board [n + 1] == board [n + 2] == "X":
                print_board(board)
                print("           Player 1 wins           ")  
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()

        for n in [0]: # Combinations (0, 4, 8) DIAGONAL LEFT TO RIGHT
            if board [n] == board [n + 4] == board [n + 8] == "X":  
                print_board(board)
                print("           Player 1 wins           ")
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()

        for n in [2]: # Combinations (2,4,6) DIAGONAL RIGHT TO LEFT
            if board [n] == board [n + 2] == board [n + 4] == "X":  
                print_board(board)
                print("           Player 1 wins           ")
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()


    # Function to check if Computer  has won.
    def check_win_computer():
        computer_won = False
        for n in range (0, 3): # Combinations (0,3,6) (1,4,7) and (2,5,8). ALL VERTICAL COMBINATIONS
            if board [n] == board [n + 3] == board [n + 6]== "O":  
                #print_board(board)
                print("          Computer wins         ")
                computer_won = True
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()
            
        for n in (0, 3, 6): # Combinations (0,1,2) (3,4,5) (6,7,8). ALL HORIZONTAL COMBINATIONS
            if board [n] == board [n + 1] == board [n + 2] == "O":  
                #print_board(board)
                print("          Computer wins         ")
                computer_won = True
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()

        for n in [0]: # Combinations (0, 4, 8) DIAGONAL LEFT TO RIGHT
            if board [n] == board [n + 4] == board [n + 8] == "O":  
               #print_board(board)
                print("          Computer wins         ")
                computer_won = True
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()

        for n in [2]: # Combinations (2,4,6) DIAGONAL RIGHT TO LEFT
            if board [n] == board [n + 2] == board [n + 4] == "O":  
               # print_board(board)
                print("          Computer wins         ")
                computer_won = True
                # CLI decoration
                decoration()
                open = input(" Thanks for playing. Hit ENTER to continue. ")
                play_again()
                exit()


    # Defining a function for Player's moves
    def player1():
        try:
            move = int(input("Player 1, enter your move (1-9): "))
        
        # Error-handling for if the input is not an integer 
        except ValueError:
            print("Invalid move. Your play must be a number")
            player1()
            return
        
        if move in unplayed_board:
            unplayed_board.remove(move)
            board[move - 1] = "X"
            player_spaces.append(move)
        else:
            print("Invalid move. Try again.")
            player1()

    # Defining a function to print the board for player 1's turn
    def player_turn():
        player1()
        print_board(board)
        minor_clear_screen()

    # Calling the player's first move
    player_turn()
    minor_clear_screen()


    # Computer's first move. will be random spot, as this move is not important strategically
    def computer_move():
        # Picking random from unplayed spots
        c_move_1 = random.choice(unplayed_board)
        # Removing played move from unplayed move, and playing.
        unplayed_board.remove(c_move_1)
        board[c_move_1 - 1] = "O"

    # Calling Computer's first move
    minor_clear_screen()
    computer_move()
    loading_dots()
    print_board(board)
   
    # Player's second move
    player_turn()

    # Computer's second move (Strategically important)
    # The user has played two moves by now, so the set player_spaces includes two elements
    # This function checks if the user is about to win by playing a full line (row, column or diagonal) 
    # The programme then identifies the line (named 1), and identifies the remaining box, and plays it, in order to block the user's win.

    def computer_move_2():
        
        # Creating an object, row, to help check which row the user is about to win on
        global row
        row = None

        # Checks if user is about to win by playing a full ROW 
        if set(player_spaces) in [{2,3}, {1,3}, {1,2}]:
            row = [1, 2, 3]

        elif set(player_spaces) in [{4,5}, {5,6}, {4,6}]:
            row = [4, 5, 6]

        elif set(player_spaces) in [{7, 8}, {8, 9}, {7, 9}]:
            row = [7, 8, 9]

        # Checks if user is about to win by playing a full COLUMN 
        elif set(player_spaces) in [{1,4}, {1,7}, {4,7}]:
            row = [1, 4, 7]

        elif set(player_spaces) in [{2,5}, {5,8}, {2,8}]:
            row = [2, 5, 8]

        elif set(player_spaces) in [{3, 6}, {6, 9}, {3, 9}]:
            row = [3, 6, 9]
        
        # Checks if user is about to win by playing a full DIAGONAL
        elif set(player_spaces) in [{1,5}, {5,9}, {1,9}]:
            row = [1, 5, 9]

        elif set(player_spaces) in [{3,5}, {5,7}, {3,7}]:
            row = [3, 5, 7]

        # Choosing Computer's move based on the above, by eliminating Players's spaces from the identified row.
        # Finding the remaining box the user will need to play to win (The indent structure below is important)
        if row:
            for x in player_spaces:
                if x in row:
                    row.remove(x)

            # Playing that box 
            chosen_move_2 = row[0]
        
        else:
            chosen_move_2 = random.choice(unplayed_board)

        # Otherwise, playing a random available move if the chosen move is not available (e.g. if Computer played it earlier)
        if chosen_move_2 in unplayed_board:
            unplayed_board.remove(chosen_move_2)
            board[chosen_move_2 - 1] = "O"
        else:
            chosen_move_2 = random.choice(unplayed_board)
            unplayed_board.remove(chosen_move_2)
            board[chosen_move_2 - 1] = "O"


    # Implementing the computer_move_2 function
    computer_move_2()
    loading_dots()
    print_board(board)

    # Player's third move
    player_turn()
    print_board(board)

    # Checking if the player has won after the player's thrid move (as the player can only win after at least three moves)
    check_win_1()

    # Computer's thrid move
    def computer_move_3 ():
        # Checks if the player is about to win by playing a full ROW, COLUMN, or DIAGONAL
        # This lists the EIGHT winning combinations
        row_1 = [1, 2, 3]
        row_2 = [4, 5, 6]
        row_3 = [7, 8, 9]
        column_1 = [1, 4, 7]
        column_2 = [2, 5, 8]
        column_3 = [3, 6, 9]
        diag_1 = [1, 5, 9]
        diag_2 = [3, 5, 7]

        # groups is a list of the winning combinations defined above
        groups = [row_1, row_2, row_3, column_1, column_2, column_3, diag_1, diag_2]
    
        for group in groups:
            # Checks if there are exactly two common elements between player_spaces (boxes the player has played by now) and the group (the winning groups listed above)
            if len (set(player_spaces) & set(group)) == 2:
                # Identifying the third element in the group and adding it to the list 'remainder'
                remainder = [w for w in group if w not in player_spaces]
                # Checking that these remainders are not yet played,(by checking they are in the unplayed board list) and adding them to a new list playable_remainder
                playable_remainder = [a for a in remainder if a in unplayed_board]
        
        # Picking a chosen move from the playable remainder. If there are multiple (unlikely), this simply picks the first
        # If the playable remainder set is empty, Computer makes a random move from the "unplayed board"
        if playable_remainder:   
            chosen_move_3 = playable_remainder[0]
        else:
            chosen_move_3 = random.choice(unplayed_board)

        # Making the play
        unplayed_board.remove(chosen_move_3)
        board[chosen_move_3 - 1] = "O"

    # Calling the function for Computer's third move
    minor_clear_screen()
    computer_move_3()
    loading_dots()
    print_board(board)

    # Check for Computer's win after Computer's thrid move
    check_win_computer()

    # Player's fourth move
    player_turn()
    minor_clear_screen()

    # Checking win after player's fourth move
    check_win_1()


    # Computer's fourth move - A random available move
    def computer_move_4():
        chosen_move_4 = random.choice(unplayed_board)
        # Making the play
        unplayed_board.remove(chosen_move_4)
        board[chosen_move_4 - 1] = "O"


    computer_move_4()
    loading_dots()
    print_board(board)

    # Check win after Computer's fourth  move
    check_win_computer()

    # Player's fifth move (must be the last move, if played at all)
    player_turn()
    minor_clear_screen()

    # Checking win after player's fifth move
    check_win_1()

    # Ending the game due to a draw (When all boxes are filled, so the list unplayed_board is empty, but there is no winner)
    if not unplayed_board:
        print("*********        IT'S A DRAW         ******")

        # CLI decoration
        decoration()

        # This keeps the programme open unitl the user hits ENTER
        open = input(" Thanks for playing. Hit ENTER to Continue. ")

    # Calling the function play_again() to check if the user wants to play again
    play_again()


# Calling the game play function to start the game
game_play()