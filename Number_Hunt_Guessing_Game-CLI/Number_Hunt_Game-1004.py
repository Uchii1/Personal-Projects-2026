# Programme Title: Number Hunt Guessing Game
# Developed by: U.C. Obiagwu, April 2026

# Importing relevant modules
import random
import time
import pyfiglet

# A ASCII art for decorative title using pyfiglet module
def title():
    print(pyfiglet.figlet_format("Number Hunt", font="slant"))

# Function to print game instructions - this is called only once each time the programme is opened
def instructions():
    print("Try to guess the Special Number, which is a random natural number from 1 to 100 inclusive.")
    time.sleep(0.75)
    print("After each guess, I'll let you know if your guess is higher or lower than the special number.")
    time.sleep(1)    

# Main Game Play Function
def main_game_play():

    # Selecting the special number as a random integer between 1 and 100
    special_number = random.randint(1, 100)

    # Funtion to receive guess and evaluate correctness
    def receive_guess():
        
        # Receiving the guess as a float and checking it is an integer with a try/except block and the recursive function receive_guess()
        try:
            guess = float(input("Enter guess: "))
        except ValueError:
            print("Invalid input. Please try again with a numerical response between 1 and 100.")
            receive_guess()
         
        # Converting guess from a float to an integer
        guess = int(guess)

        # Comparing the guess to the special number
        if guess != special_number:
            incorrect_guess(guess)
        elif guess == special_number:
            print("Correct")
            check_user_wants_to_play_again()
            
    # Function to handle incorrect guesses
    def incorrect_guess(guess):
        if guess > special_number:
            print(f"{guess} is Too High")
            receive_guess()

        elif guess < special_number:
            print(f"{guess} is Too Low")
            receive_guess()
        else:
            print("Error") # Not expected to be run
            pass

    # The below is run first within the function.
    # Choosing the special number
    print ("\n \nLoading Speial Number", end="")
    for i in range (3):
        print(".", end="", flush = True)
        time.sleep(0.75)  # 0.75 seconds between the dots.
    #time.sleep(0.5)
    print("\n \nThe Special Number has been chosen. Try to guess it")
    receive_guess()

# Defining the main programme function
def programme_run():

    # Checking if the user wants to play again
    again = None # Not necessary, but good practice, as again will be a global function
    global check_user_wants_to_play_again
    def check_user_wants_to_play_again():
        global again
        again = input("Would you like to play again? \n[1] Yes! :) \n[2]No :( \n ")
        again = int(again)
        if again == 1:
            main_game_play()
        else:
            confirm_exit()

    # Defining and calling a function to confirm the user wants to exit.
    def confirm_exit():
        if again == 1:
            main_game_play()
        else:
            confirm = input("Are you sure you want to exit? \n[1] No, I want to play on! \n[2] Yes :( \n")
            confirm = int(confirm)
            if confirm == 1:
                main_game_play()
            else:
                print("Bye! Play again Soon!")
                time.sleep(0.5)
                stayopen = input("Hit Enter to Exit")
                exit()  

    # Defining the order of functions for the programme run
    title()
    instructions()
    main_game_play()
    check_user_wants_to_play_again()
    confirm_exit()

# Calling the main function, programme_run() to start the programme
programme_run()