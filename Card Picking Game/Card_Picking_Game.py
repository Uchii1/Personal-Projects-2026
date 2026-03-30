import random
import time

computer_set = [2, 3, 4, 5, 6, 7, 8, 9, 10]
player_set = [2, 3, 4, 5, 6, 7, 8, 9, 10]
computer_chosen = []
player_chosen =[]

print(" ")
print("WELCOME TO CLI BLACKJACK")
print("You can pick two or three random cards. The computer picks the same number of cards as you.")
print("The goal is to have cards summing up to 21 or less, and with a higher sum than the computer's")
print(" ")


def decorative_loading(n):
    print("Loading", end=" ")
    for i in range(1, 4):
        time.sleep(n)
        print(".", end=" ", flush= True)
    print(".")


def player_turn():
    # chooses a random card for the player
    placeholder = input("Hit ENTER to choose your card: ")
    player_choice_1 =random.choice(player_set)

    # stores chosen card in appropriate list
    player_set.remove(player_choice_1)
    player_chosen.append(player_choice_1)

    # informs player of their card
    decorative_loading(0.5)
    print(f"YOUR CARD(S): {player_chosen}")

# Round 1
print("ROUND 1")
player_turn()


def computer_turn_1():
    print(" \nComputer is choosing first card")
    # calling the decorative loading function, with 0.5 seconds between dots.
    decorative_loading(0.5)

    # choosing first card
    chosen_card_1 = random.choice(computer_set)
    chosen_card_1 = int(chosen_card_1)
    computer_set.remove(chosen_card_1)
    computer_chosen.append(chosen_card_1)
    print(f"Computer's first card:{chosen_card_1}")

computer_turn_1()


# Round 2
print(" \nROUND 2")
player_turn()


# Computer's second card
def computer_turn_2():
    print(" \nComputer is choosing second card")
    # calling the decorative loading function, with 0.5 seconds between dots.
    decorative_loading(0.5)
    
    # chosing second card
    chosen_card_2 = random.choice(computer_set)
    chosen_card_2 = int(chosen_card_2)
    computer_set.remove(chosen_card_2)
    computer_chosen.append(chosen_card_2)
   
computer_turn_2()


# Checking for round 3
# defining function to choose computer's thrid card
def computer_turn_3():
    print(" \nComputer is choosing third card")
    # calling the decorative loading function, with 0.5 seconds between dots.
    decorative_loading(0.5)

    # choosing third card
    chosen_card_3 = random.choice(computer_set)
    chosen_card_3 = int(chosen_card_3)
    computer_set.remove(chosen_card_3)
    computer_chosen.append(chosen_card_3)


# Players third card
def player_turn_3():
    print(" ")
    print("Would you like a third round?")
    third_pick_choice = input("[1] = Yes \n[2] = No\nEnter: ")
    third_pick_choice = int(third_pick_choice)

    try:
        if third_pick_choice == 1:
            # if the user opts for a third round
            print(" ")
            print("ROUND 3")
            player_turn()
            # This calls the function to choose the computer's thrid card
            computer_turn_3()
        elif third_pick_choice != 1 and third_pick_choice != 2:
            print("Please enter a valid input")
            time.sleep(0.5)
            player_turn_3()
        else:
            print("Ending game...")
    except ValueError:
        print("Please enter a valid input")
        player_turn_3()
    except:
        print("Please enter a valid input")
        player_turn_3()

player_turn_3()


# Printing Computer's full hand
def print_computer_full():
    print(" ")
    print(f"The computer's full cards are:", end=" ", flush=True)
    for i in computer_chosen:
        time.sleep(1)
        print(f"{i}", end=", ", flush= True)
    time.sleep(1)
    computer_sum= sum(computer_chosen)
    print(f"\nSum of computer's cards: {computer_sum}")
    time.sleep(2)
print_computer_full()


# Comparing hands to declare a winner
def check_winner():
    print(" ")
    print(f"Player's cards are:", end=" ", flush=True)
    for i in player_chosen:
        time.sleep(1)
        print(f"{i}", end=", " , flush=True)
    time.sleep(1)
    player_sum = sum(player_chosen)

    # the variable computer_sum needs to be redefined here
    computer_sum = sum(computer_chosen)

    # printing player's sum
    print(f"\nThe sum of player's cards are: {player_sum}")

    # blank line and pause for neatness
    print(" ")
    time.sleep(1)
    # checking for a winner
    if (computer_sum > 21) and (player_sum > 21):
        print("Game Over It's a draw")
    if player_sum > 21:
        print("Game Over. Computer Won")
    elif (player_sum < 21) and (player_sum > computer_sum):
        print("You won!")
    else:
        print("Computer wins. Try again")
    # some blank lines for neatness
    print(" \n \n ")

check_winner()
stay_open = input("Thanks for playing! \nHit ENTER to exit.")