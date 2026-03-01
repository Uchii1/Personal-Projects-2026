# Password Generator Using Python Random Module

import random

# Function to confirm password length
def ascertain_length():
    # The length is stored as w, which will be made global, so it can be used in another function
    global w

    w = input("How long do you want your password?\n Password length: ")
    print(" ")  # blank space for neatness
    # Converting w to an integer
    w = int(w)

    if w <= 5:
        print(f"The recommended length is at least 6 characters. {w} characters is too short.")
        print(" ") # blank line for neatness
        ascertain_length()
    elif w > 20:
        print(f"The recommended length is at most 20 characters. {w} characters is too long ")
        print(" ")  # blank line for neatness
        ascertain_length()
    else:
        print(f"Great! {w} letters works")
        print(" ") # blank line for neatness


# Function to create the password
def create_password():
    # The list named 'store' will hold the password
    store = []
    
    # This ensures the first character of the password is a letter
    first = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    store.append(first)

    # The below generates and appends additional characters
    v = w - 1
    for i in range(v):
        x = random.choice('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!()?/')
        store.append(x)

    # Joining the characters in the list store to make a password
    pass_code = ''.join(store)
    print(f"Here is your password: {pass_code}")
    print(" ") # blank line for neatness


# Checking if the user wants to repeat
def check_repeat():
    repeat = input(" Would you like to do this gain? \n1.Yes \n2.No \nInput (1 - 2): ")

    if repeat == "1":
        run_full_programme()
    elif repeat == "2":
        stayopen = input("Thanks for using the Password Generator. Press ENTER to exit")
        exit()
    else:
        print("Invalid input. Please enter a valid input, (Either 1 or 2)")
        print(" ") # blank line for neatness
        check_repeat()


# This function runs the full programme 
def run_full_programme():

    # Checking the desired password length
    ascertain_length()

    # Calling the function to create the password
    create_password()

    # Calling the function to check if the user wants to run the programme again
    check_repeat()


# The below is executed when the programme is opened and it runs the full programme
run_full_programme()

