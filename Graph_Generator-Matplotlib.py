# FITNESS DATA GRAPHING PROGRAMME


# INTRODUCTION
# A Python programme to collect inputs of personal fitness data and produce helpful graphics with Matplotlib


# RELEVANT MODULES
import json
import os
import matplotlib.pyplot as plt
import pyfiglet
import time


# DATA HANDLING
# Loading long-term storage (JSON file)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Pedometer data
PedometerData = os.path.join(script_dir,'PedometerData.json')

# Calorie data
FoodData = os.path.join(script_dir, 'FoodData.json')


# Function to load pedometer data
# The load_pedometer_data() function is only called within other functions and not on its own
def load_pedometer_data():
    try:
        with open(PedometerData, "r") as f: # This opens and reads the local file PedometerData.json, and returns the data in it.
            return json.load(f)
        
    # return list of days if this is not found
    except (json.JSONDecodeError, FileNotFoundError):
        return {"weekly_graph": {"Sunday": [], "Monday": [], "Tuesday": [],
                                  "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": []}}
    
# Function to save pedometer data
# The save_pedometer_data() function is only called within other functions and not on its own
def save_pedometer_data(overall):
    with open(PedometerData, "w") as f:  # This opens and writes to PedometerData.json, and edits the data in it.
        json.dump(overall, f, indent=1)  # The JSON file will be indented by 1 space for readability


# Function to load calorie data
# The load_calorie_data() function is only called within other functions and not on its own
def load_calorie_data():
    try:
        with open(FoodData, "r") as f: # This opens and reads the local file FoodData.json, and returns the data in it.
            return json.load(f)
        
    # return list of days if this is not found
    except (json.JSONDecodeError, FileNotFoundError):
        return {"weekly_graph": {"Sunday": [], "Monday": [], "Tuesday": [],
                                  "Wednesday": [], "Thursday": [], "Friday": [], "Saturday": []}}

# Function to save calorie data
# The save_calorie_data() function is only called within other functions and not on its own
def save_calorie_data(overall):
    with open(FoodData, "w") as f:  # This opens and writes to FoodData.json, and edits the data in it.
        json.dump(overall, f, indent=1)  # The JSON file will be indented by 1 space for readability


# USER INTERFACE HANDLING
# General screen clearing that clears the whole screen, except for the heading
def screen_clearing():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pyfiglet.figlet_format("Fitness Tracker", font="slant"))
    print(" ")


# Main menu function
def main_menu():
    print( "    MAIN MENU")
    print(" \nWhat would you like to do?")
    print("[1] Input Data \n[2] View Data \n[3] Exit")
    choice = input("Enter Your Choice:  ")

    # An inner function to receive input
    def enter_choice(choice):
        try:
            choice = int(choice.strip())

            if choice == 1:
                screen_clearing()
                input_data_submenu()
                
            elif choice == 2:
                screen_clearing()
                view_data_submenu()
                
            elif choice == 3:
                screen_clearing()
                exit_confirmation()
            
            # If the input is an integer outside of the menu options...
            else:
                print("The choice must be a one of the integers (1 - 3) listed in the menu\n ")
                choice = input("Enter your choice: ")  # Reassigning choice to the new input
                enter_choice(choice)

        except ValueError :
                print(" Please enter valid input as your choice\n ")
                time.sleep(1)  # One second pause to allow user to read error message
                choice = input("Enter your choice: ")  # Reassigning choice to the new input
                enter_choice(choice)  # Calls enter_choice recursively.

    enter_choice(choice)


# INPUT DATA SUBMENU FUNCTION
def input_data_submenu():
    print("INPUT DATA")
    print(" \nWhat would you like to do?")
    print("[1] Input Pedometer Data \n[2] Input Calorie Data \n[3] Return to Main Menu \n[4] Exit the Programme ")
    choice_input_data = input("Enter Your Choice...")
    choice_input_data = int(choice_input_data.strip())

    if choice_input_data == 1:
        screen_clearing()
        input_pedometer_data()
        
    elif choice_input_data == 2:
        screen_clearing()
        input_calorie_data()
        
    elif choice_input_data == 3:
        screen_clearing()
        main_menu()

    elif choice_input_data == 4:
        exit_confirmation()
    
    else:
        print("Invalid choice entered. Please try again")
        time.sleep(0.75)  # Pause to allow user to read the message above.
        screen_clearing()
        input_data_submenu()

      
# FUNCTION TO INPUT PEDOMETER DATA
def input_pedometer_data():
    week_list = load_pedometer_data()

    # Clearing stale data from previous use
    for day in week_list[0]["weekly_graph"]:
        week_list[0]["weekly_graph"][day] = []
    save_pedometer_data(week_list)

    # Returning the keys in the "weekly-graph" dictionary as a list
    days = list(week_list[0]["weekly_graph"].keys())

    # Inputting the data
    print("Enter the steps taken for each day of the past week (\n (press Enter to skip, e.g, if you did not take a walk that day.):\n")
    for day in days:
        steps = input(f"Steps on {day}: ")

        # The below runs if there is input. It adds the number of steps to the weekly-graph dictionary
        if steps.strip().isdigit():
            week_list[0]["weekly_graph"][day].append(int(steps))
        else:
            print(f"No valid step figures entered for {day}. 0 steps assumed.")
    
    # This saves the updated list
    save_pedometer_data(week_list) 

    # Confirms the saving of the list.
    print("\nSaved! Pedometer data:")
    for day, steps in week_list[0]["weekly_graph"].items():
        print(f"  {day}: {steps}") 
    
    # returning to main menu
    screen_clearing()
    main_menu()
       

# FUNCTION TO INPUT CALORIE DATA
def input_calorie_data():
    calorie_week_list = load_calorie_data()

    # Clearing stale data from previous use
    for day in calorie_week_list[0]["weekly_graph"]:
        calorie_week_list[0]["weekly_graph"][day] = []
    save_calorie_data(calorie_week_list)

    # Returning the keys in the "weekly-graph" dictionary as a list
    days = list(calorie_week_list[0]["weekly_graph"].keys())

    print("Enter steps for each day (press Enter to skip):\n")

    # Inputting the data
    for day in days:
        calories = input(f"kCal on {day}: ")

        # Appends data to json file if there is input. Adds the number of steps to the weekly-graph dictionary
        if calories.strip().isdigit():
            calorie_week_list[0]["weekly_graph"][day].append(int(calories))
        else:
            print(f"No valid calories entered for {day}. 0 calories assumed")

    # Saves the updated list
    save_calorie_data(calorie_week_list) 

    print("\nSaved! Calorie data:")
    for day, calories in calorie_week_list[0]["weekly_graph"].items():
        print(f"  {day}: {calories}") 
    
    # After this the programme runs the begin_programme function(), returning to main menu
    # returning to main menu
    screen_clearing()
    main_menu()


def line_graph():
    # A Graph Showing personal pedometer data this week

    # Source data
    calorie_data = load_calorie_data()
    step_data = load_pedometer_data()
    days   = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat",]

    # The 'if v' wording below handles a situation where there is no input for a day (i.e. an empty value)
    steps    = [v[0] if v else 0 for v in step_data[0]["weekly_graph"].values()]
    calories = [v[0] if v else 0 for v in calorie_data[0]["weekly_graph"].values()]


    plt.plot(days, steps, label="Steps")
    plt.plot(days, calories, label="Calories")
    plt.legend()
    plt.show()
    
    # returning to main menu
    screen_clearing()
    main_menu()


# SUBMENU TO VIEW DATA IN LINE GRAPHS
def view_data_submenu():
    print("VIEW DATA")
    print(" \nWhat would you like to view ?")
    print("[1] Pedometer Line Graph \n[2] Calorie Line Graph \n[3] Pedometer and Calorie Combined Graph \n[4] Return to Main Menu \n[5] Exit the Programme ")
    choice_view_data = input("Enter Your Choice...")
    choice_view_data = int(choice_view_data.strip())

    if choice_view_data == 1:
        screen_clearing()
        view_pedometer_data()
        
    elif choice_view_data == 2:
        screen_clearing()
        view_calorie_data()
        
    elif choice_view_data == 3:
        screen_clearing()
        view_pedometer_and_calorie_data()
        
    elif choice_view_data == 4:
        screen_clearing()
        main_menu()

    elif choice_view_data == 5:
        screen_clearing()
        exit_confirmation()

    # Returning to main menu
    screen_clearing()
    main_menu()
        

# FUNCTION TO VIEW PEDOMETER DATA
def view_pedometer_data():

    # Source data
    step_data = load_pedometer_data()
    days   = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat",]
  
    # The 'if v' wording below handles a situation where there is no input for a day (i.e. an empty value)
    steps    = [v[0] if v else 0 for v in step_data[0]["weekly_graph"].values()]

    plt.plot(days, steps, label="Steps")
    plt.legend()
    plt.show()

  


# FUNCTION TO VIEW CALORIE DATA
def view_calorie_data():

    # Source data
    calorie_data = load_calorie_data()

    days   = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat",]

    calories = list(calorie_data[0].keys())

    # The 'if v' wording below handles a situation where there is no input for a day (i.e. an empty value)
    calories = [v[0] if v else 0 for v in calorie_data[0]["weekly_graph"].values()]

    plt.plot(days, calories, label="Calories")
    plt.legend()
    plt.show()

    # returning to main menu
    screen_clearing()
    main_menu()

# FUNCTION TO VIEW PEDOMETER DATA AND CALORIE DATA GRAPHED TOGETHER
def view_pedometer_and_calorie_data():
    screen_clearing()
    line_graph()  # line_graph() reverts back to main menu
  

def exit_confirmation():
    print("Placeholder")
    confirm_exit = input("Are you sure you want to exit? \n[1] Yes \n[2] No \nEnter your choice: ")
    try:
        confirm_exit = int(confirm_exit)
    except ValueError:
        print("Please enter a valid input")
        exit_confirmation()

    # Confirming exit and executing exit() if confirmed
    if confirm_exit == 1:
        stay_open = input(" \nThanks for using the programme. Press ENTER to exit")
        exit()

    else:
        main_menu()

def begin_programme():
    screen_clearing()
    main_menu()

begin_programme()
