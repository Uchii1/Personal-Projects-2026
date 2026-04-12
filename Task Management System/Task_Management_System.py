# SOFTWARE DEVELOPMENT PROJECT
# A CLI task manager with functionality to add tasks, mark them as complete, display a list of tasks, and delete tasks from the list

# Python imports a JSON file named "saved_tasks.json" to store the tasks
import json
# The os function provides path-finding and file-handling abilities for the programme
import os

# The time module supports the decorative loading function in the list_tasks() function (Main menu option 3)
import time

# Path to folder that should contain file 
script_dir = os.path.dirname(os.path.abspath(__file__))
SAVEDTASKS= os.path.join(script_dir, 'saved_tasks.json')
# SAVEDTASKS is the JSON file: 'save_tasks.json'


# THE FUNCTIONS WILL INCLUDE: LOAD, ADD, LIST, MARK COMPLETE, DELETE

# FUNCTION TO LOAD TASKS
# The load_tasks() function is only called within other functions and not on its own
def load_tasks():
    if os.path.exists(SAVEDTASKS):
        with open(SAVEDTASKS, "r") as f:  # This opens and reads saved_tasks.json, and returns the data in it.
            return json.load(f)
    return []


# FUNCTION TO SAVE TASKS
# The save_tasks() function is only called within other functions and not on its own
# When the save_tasks() function is called below, this will save the task to the json file
def save_tasks(tasks):
    with open(SAVEDTASKS, "w") as f:  # This opens and writes to saved_tasks.json, and edits the data in it.
        json.dump(tasks, f, indent=1)  # The JSON file will be indented by 1 space for readability


# FUNCTION TO PRINT A STANDARD LOADING SEQUENCE FOR THE PROGRAMME - This prints three dots 0.3 seconds apart
# The loading sequence will signify a new part of the programme is being opened.
def loading_sequence():
    for i in range(3):
        print(".", end= "", flush = True)  # The flush keyword ensures the dots are printed at each iteration of the loop
        time.sleep(0.3) # There are 0.3 seconds between the dots being displayed.
    print(" ")  # A blank line is left for neatness


# FUNCTION TO ADD TASKS
def add_tasks(description):  # The user will enter description when adding tasks
    print(" ")  # Blank line left for neatness
    urg = input("Enter urgency: \n 3: High \n 2: Medium \n 1: Low \n \nIf nothing is entered, Low urgency will be assumed.\nEnter Urgency(1-3): ").strip()
    if urg == "3":
        urgency = "High"
    elif urg == "2":
        urgency = "Medium"
    else:
        urgency = "Low"  # The programme assumes low urgency if the user does not enter 3 or 2

    tasks = load_tasks()
    # Below, a task entry is created the id if chronological and the completed status is automatically false. The description is the text entered by the user.
    task = {
        "id": len(tasks) +1,
        "description": description,
        "urgency": urgency,
        "completed": False
    }
    tasks.append(task) # Append adds the newly created task to the end of the tasks list
    save_tasks(tasks)  # This function rights the task to the JSON file for long-term storage
    print(f"New Task Added: {description}")
    add_more() # This calls the add_more function below to ask user if they want to add more tasks


# FUNCTION TO CHECK IF THE USER WANTS TO ADD MORE TASKS
def add_more():
    add_another = input("\n Would you like to add another task? ( 1 = Yes, 0 = No ) \n Enter choice: ").strip()
    if add_another == "1":
            description = input("Enter task description: ")
            add_tasks(description)
    else:
        print("Returning to main menu...")
        print ("Loading", end="")
        loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.
        mainmenu("")  # Returns to main menu if user does not type in "1"

       
# FUNCTION TO LIST ALL TASKS
def list_tasks():  # This lists the tasks without listing the options
    
    # The below is a mainly decorative loading text
    print(" ")
    print ("Loading tasks", end="")
    loading_sequence()  # This prints the time-separated dots, as programmed in the loading sequence function above
    
    # Lists the tasks via the load_task function defined above
    tasks = load_tasks()  

    if not tasks:
        print("Tasks list is empty")
        return
    
    # This indexes the tasks
    for i, task in enumerate(tasks, start=1):
        task["id"] = i  # Here, the task id is renumbered from 1
        save_tasks(tasks)  # This calls the save_tasks function defined above, which saves the JSON file again
    
    print("\n")
    print(("="*20) + "TASK LIST" + ("="*20) + "\n")
    print(" STATUS - ID -----URGENCY -- DESCRIPTION")

    for task in tasks:
        # This prints the tasks neatly. The task id is printed as 2 digits for consistency. 
        status = "✓" if task["completed"] else "O"  # Shows a tick beside the task if the boolean value in the task completed field is True, and a O otherwise.
        print(f"  {status:1}{'':<5} [{task['id']:02d}] {'':<4} {task['urgency']:6} {'':<3} {task['description']}")
    print("="*50 + "\n")  # A decorative line for neatness


# FUNCTION TO DISPLAY OPTIONS - TO BE USED AFTER LISTING TASKS
def post_list_options():  # Below, entering [2], or any input apart from [1], will return the user to the main menu
    post_list = input("Would you like to \n [1] Mark a task as complete \n [2] Return to Main Menu \n Enter choice (1-2): ").strip()
    if post_list == "1":
        try:
            print(" ")  # Blank line for neatness
            task_id = int(input("Enter the ID of the task to mark complete: "))
            complete_tasks(task_id)  # Calls the complete_tasks function defined below.
            post_list_options()  # Returns to post list options after completing a task (Makes the function recursive)

        # This catches exceptions and returns the user to the start of the post_list_options() function
        except ValueError:
            print("Invalid task ID")
            print(" The task ID must be a valid number from those above. Please try again.", end = " ")
            loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.


        # The below catches exceptions not caught above, and returns the user to the start of the function
        except Exception as e:
            print(f"Error: {e}")
            print(" The task ID must be a valid number from those above. Please try again.", end = " ")
            loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.

    else:
        print(" ")  # Blank line for neatness
        # The below is time-measured decorative text
        print("Returning to main menu. Loading", end =" ") # The end keyword prints the following output on the same line
        loading_sequence()  #  This prints the time-separated dots defined in the loading sequence above.
        mainmenu("")  # Returns to main menu if user enters 2

# FUNCTION TO DISPLAY BOTH TASKS AND OPTIONS
def list_tasks_and_options():  # This lists both the tasks and the post-list options
    list_tasks()  # This calls the list tasks function defined above   
    post_list_options()  # This calls the post list options function defined below


# FUNCTION TO MARK TASKS AS COMPLETE
# A list of available tasks is displayed and the user is prompted to enter the ID (task_id) of the task to be marked complete
def complete_tasks(task_id):
    tasks = load_tasks() # This calls the load_tasks function defined above, so the relevant task can be found among those available
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:  # This checks whether the selected task is already marked complete
                print(" ")  # A blank line for neatness
                # The end=" " command will print the join the next line to this one
                print(f"Task {task_id} is already marked complete. Returning to menu", end=" ")
                loading_sequence()  #  This prints the time-separated dots defined in the loading sequence above.
                mainmenu("")  
                
            elif not task["completed"]:  # Triggered if the tasks exists and is not marked completed.
                task["completed"] = True
                save_tasks(tasks)
                print(" ")  # A blank line for neatness
                print(f"✓ Task {task_id} is now marked complete. Well done for completing a task!")
                time.sleep(0.3)  # This makes the programme pause before printing the next line, giving the user reading time
                print("Returning to main menu...", end = "")
                loading_sequence()  # The pre-set loading sequence funtion is used here
                print(" ")  # A blank line for neatness
                # Some decoration
                for y in range (1,4):
                    w = 4 - y
                    time.sleep(0.4) # 0.4 seconds between each line of dots being displayed. The time module is used
                    print((("*"*y)+(" "*(2*w))+("*"*y))*11)
                    print(" ")
                mainmenu(" ")

    # If the task is not found, the following error message is returned. And the programme returns to the main menu
    if ValueError:
        print(" ")  # A blank line is left for neatness
        print(f"Value error: Task {task_id} was not found. Please check your input.")
        print(" ")
        print("Returning to main menu", end = "")
        loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.
        
    else:
        print(" ")  # A blank line is left for neatness
        print(f"Error found: Task {task_id} was not found. Check that your input is a number")
        print(" ")
        print("Returning to main menu", end = "")
        loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.


# FUNCTION TO DELETE TASKS FROM THE LIST
def delete_tasks(task_id):
    tasks = load_tasks() # This calls the load_tasks function defined above, so the relevant task can be found among those available
    
    be_deleted = None  # A variable is defined to be assigned to hold the task to be deleted.

    for task in tasks:
        if task["id"] == task_id:
            be_deleted = task  # This assigns the variable be_deleted to the chosen task, so it can be deleted safely
            break
            
    if task == be_deleted:  # This checks if each task is the chosen task to be deleted
        tasks.remove(be_deleted)  # This removes the chosen task from the tasks list

        # This reindexes tasks after deletion of a task, and before saving:
        for i, task in enumerate(tasks, start =1):
            task["id"] = i  # Here, task IDs is renumbered from 1
        save_tasks(tasks)  # This calls the save_tasks function defined above, which saves the json file again
        print(f"Done! Task {task_id} has been deleted")
        print(" ")  # Blank line for neatness
        print("Returning to the main menu", end=" ")
        loading_sequence()  # This prints the time-separated dots defined in the loading sequence above
        return  # Exits after deleting
    
    else:
        print("\nError: The chosen task was not found")  # This is printed when the task is not found through the IF statement above
        print(" ")  # A blank line left for neatness
        # The below is a mainly decorative loading text
        print("Returning to the main menu", end=" ")
        loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.


# FUNCTION TO CALL THE MAIN MENU
def mainmenu(menu_choice):  # This defines the main menu function
    while True:
        print ("\n === Main Menu === ")
        print("1. Add a Task ")
        print("2. List all Tasks ")
        print("3. Mark a Task as Complete ")
        print("4. Delete a Task from List ")
        print("5. Exit the Task Manager ")
        print("======================")
        menu_choice = input("\n Enter a choice from above (1-5): ").strip()

        # The user's menu choice is accepted as a string.
        if menu_choice == "1":
            desc = input("\nPlease enter the task description: \nTask Description: ")
            # The IF statement triggers the add_task() function if a valid name is entered. 
            # The IF statement can also print an error message or handle an exception if no input is entered
            if desc:
                try:
                    add_tasks(desc)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Task description must be entered.") 
  
        elif menu_choice == "2":  # This lists all tasks
            list_tasks_and_options()
        
        elif menu_choice == "3":  # This marks a specified task as complete
            list_tasks()
            try:
                task_id = int(input("From the list above, enter the ID of the task to mark complete. Enter 0 to quit and return to main menu \nTask ID: "))
                if task_id == 0:  # This gives the user the option to exit the "mark complete" procedure
                    print("No task marked complete. Returning to main menu")
                    # The below is a mainly decorative loading text - a slightly shorter loading sequence than loading_sequence()
                    print ("Loading", end="")
                    for i in range(3):
                        print(".", end= "", flush = True)
                        time.sleep(0.1) # 0.1 seconds between the dots being displayed. The time module is used directly.
                    print(" ")  # A blank line left for neatness
                    mainmenu(" ") # Main menu is called here, as the user does not want to mark a task complete.
                else:
                    complete_tasks(task_id)

            # This is triggered when input is of a valid type, but invalid value
            except ValueError:  
                print("")
                print("Invalid task ID.The task ID must be a valid number from those above. Return to main menu and try again.")
                # Returning to main menu
                print ("Returning to main menu", end="")
                loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.
                mainmenu("")  # Returns to the the main menu 

            # This will catch exceptions not detected by ValueError, return an error message, and return to main menu
            except Exception as e:  
                print(f"Error: {e}")  # Prints the exception found before printing the programme's standard error message.
                print("The task ID must be a valid number from those above. Return to main menu and try again.")
                # Returning to main menu
                print ("Returning to main menu", end="")  # The end=" " command will print the join the next line to this one
                loading_sequence()  # This prints the time-separated dots defined in the loading sequence.
                mainmenu("")  # Returns to the the main menu      

        elif menu_choice == "4":  # This deletes a specified task
            list_tasks()  # This lists the tasks through the specified function, so the user can choose which to delete.
            try:
                task_id = int(input("From the list above, Enter the ID of the task to delete: "))
                delete_tasks(task_id)  # The specified task is removed from storage, and the remaining tasks are reindexed.
            except ValueError:  # This is triggered when input is of a valid type, but invalid value
                print("Invalid task ID. Returning to main menu.", end = " ")
                loading_sequence()  # This prints the time-separated dots defined in the loading sequence     
            except Exception as e:  # This will catch exceptions not detected by ValueError
                print(f"Error: {e}")
                loading_sequence()  # This prints the time-separated dots defined in the loading sequence 

        elif menu_choice == "5":  # Exit the task manager
            print(" \nAre you sure you want to exit the Task Manager\n [1] = Yes \n [2] = No")
            confirm = input("Enter a choice from above (1-2): ").strip()
            if confirm == "2" :
                print(" ")  # Blank line left for neatness
                print (" Great! Returning to main menu", end="")
                loading_sequence()  # This prints the time-separated dots defined in the loading sequence above.  
                print(" ")  # Blank line left for neatness
                mainmenu(" ")  # Returns to main menu if user declines to leave.

            elif confirm == "1": 
                # Requesting input 'stayopen' keeps the programme open until the user presses ENTER
                stayopen = input("Goodbye! Press ENTER to Exit. You can reopen the programme later.")  
                exit()  # This exits the programme when the user presses ENTER.  

            else:
                print("In valid choice. Please return to main menu and try again.")  # This is triggered if the input is not 1 or 2
                
                # The time module is applied below to deliver a slightly longer loading sequence than the function loading_sequence().
                # It will cause the user to pause before retrying, and avoid re-entering invalid input.
                print ("Returning to main menu", end="")
                for i in range(3):
                    print(".", end= "", flush = True)  # The flush keyword ensures the dots are printed at each iteration of the loop
                    time.sleep(0.5) # 0.5 seconds between the dots being displayed.
                mainmenu("")  # Returns to the the main menu
        
        else:# This is triggered if the input is not a valid choice. It calls the mainmenu function again if the input was not 1-5
                print(" ")
                print("Please enter a valid choice from the main menu (1-5)")
                # The longer loading sequence is also used here, to cause the user to pause before retrying
                print("Returning to main menu. Loading", end=" ")
                for i in range(3):
                    print(".", end= "", flush = True)  # The flush keyword ensures the dots are printed at each iteration of the loop
                    time.sleep(0.5) # 0.5 seconds between the dots being displayed.
                print(" ")  # Blank line for neatness
                mainmenu("")  # Returns to the the main menu  
                

if __name__ == "__main__":

    mainmenu("")  # This runs the mainmenu function when the script is executed directly, and so starts the programme
