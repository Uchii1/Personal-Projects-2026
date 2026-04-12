# README 
## TASK MANAGEMENT SYSTEM

## Introduction 

The programme is a Command Line Interface (CLI) task management system developed as part of an academic project.

Although it is a CLI programme, it has been designed to be user friendly, with  extensive error-handling capabilities, and well-designed interactive features. The programme consists of a python script and a connected JSON file for long-term data storage. 
The programme imports and uses the following modules: JSON (for data persistence), OS (for file-handling), and time (for decorative features, including a loading sequence) 

 
### Use cases 

The main aim of the programme is to help the user to record a collection of tasks and track their completion status. The programme will be useful for an individual person keeping track of personal tasks, or a professional keeping track of business-related tasks. 

A digital task management system has significant practical advantages over paper-based task management systems. A software programme makes it easier to create a list of tasks and access them flexibly. A digital system makes modifying entries cleaner and easier: tasks can be marked complete and deleted without crossing-out or erasing. Further, compared to handwritten task management systems, which are vulnerable to physical damage and misplacement, the records in an electronic system can be backed up relatively easily and so carry a lower risk of data loss. 


## Installation 

The Python script and linked JSON file can be downloaded and run directly.  

Run the programme with a CLI interpreter on Windows: 
Python C:\path\to\Task_Management_System.py 

The programme can also be run with a Python runtime software programme. 

 
## Instructions for Use 

### Main Menu 

The main menu displays the programme’s functionalities and assigns a number to each. Enter your choice as a number. This is accepted as a string and is used to call the required function within the programme. The main menu function is recursive, so if an invalid input is entered in the main menu, the main menu calls and loads itself, and you can try again. 


### Adding Tasks (Option 1 on the main menu) 

To add a task, select option 1 on the main menu. When prompted, enter the task description. Tasks are automatically assigned the next available consecutive task ID. 

You will also be prompted to enter a value for the task’s urgency on a scale of 1 (low) to 3 (high), which will be stored along with the task data and displayed in the list of tasks. If nothing is entered here, the programme assumes low urgency.  

After successfully adding a task, you can choose to add another task or to return to the main menu. 


### Viewing Tasks (Option 2 on main menu) 

To view all tasks, select option 2 on the main menu. The programme retrieves the list of tasks from the JSON file and displays them. If there are no stored tasks, a message is displayed stating this. Tasks are displayed as a table showing the task’s ID number, completion status, urgency, and description in that order. 
From this point, you can either return to the main menu or proceed to mark a task as complete.

 
### Marking Tasks as Complete (Option 3 on main menu) 

The programme will retrieve and display the list of tasks, and you can choose the task to mark complete by inputting the task ID number displayed next to it. 

 You will receive confirmation when your task has been successfully marked complete. If the inputted task ID is not valid, or the related task is already marked complete, you will receive an error message stating this and will be returned to the main menu. 

 
### Deleting a Task from the List (Option 4 on main menu) 

Tasks can be deleted from the list regardless of whether they are complete or not. The programme will display the current list of tasks, and you can select the one you want to delete. To maintain consistency and comprehensibility, the ID numbers after the deleted tasks will be reassigned, with each subsequent task shifting up one position. 

 
### Exiting the Task Manager (Option 5 on main menu) 

After selecting the exit option on the main menu, you will be asked to confirm you want to exit. If you do not confirm, you will be returned to the main menu. If you confirm you want to exit, the programme will terminate.  

Depending on your compiler software, you will then be able to close the window by pressing ENTER.  

 


## Developer Notes and Possible Future Improvements 

The programme can possibly be made more robust by including functionality to sort the tasks and display them based on a classification selected by the user. For example, a function to display only high urgency tasks, or only tasks that are not yet completed. 

 

## Assessment Requirements Analysis 

### Functionality:  

The code has been written to ensure the programme runs smoothly and inputted tasks are stored correctly. Tasks are assigned an ID number to help the programme identify them when performing functions.  

Along with adding, viewing, and marking tasks complete, the programme allows users to delete tasks from the long-term storage, avoiding clutter in the list. Also, users can classify tasks based on urgency and this classification is displayed when the tasks are listed. 


### Code quality and organisation: 

The PEP 8 style guide has been applied in the programme, particularly in the formatting of comments.

The programme uses some integral functions such as load_tasks() and save_tasks() (lines 20 - 34) to read and write data in the JSON file. Using functions instead of plain code for this helps to ensure smooth file management, and saves space because it avoids the repetition of lines of code later in the file.
The functions are logically placed, with each function being defined before it is called, to avoid execution errors. There are comments where necessary to aid understanding and possible future modification. There is also consistent indentation for neatness.

 
### Data management: 

The data is stored externally in a JSON file. Each task has a task ID. When a task is deleted, the ID numbers are automatically reindexed, helping to ensure smooth data management. 

 
### Error handling:  

There is error handling functionality within the code, including the use of exceptions such as ValueError to catch incompatible inputs and prevent the programme from crashing in these situations.  

The programme is also written to keep errors to a minimum. For example, within the add_tasks function, if a user does not enter an input for the task description, the programme returns an error message, as the task description is an integral part of the task record. However, if no input is entered for the task urgency, the programme assumes a low urgency for the task (line 55), and continues running because the task urgency is a less vital part of the task record. This approach is disclosed to the user within the instructions, and it avoids the need to raise an error message. 

 
### Documentation:  

Instructions for using the code are given within this README file for the end user. Within the code, comments are included to aid any developers who might work with the programme, and these are only placed where necessary, to reduce congestion.  

 
## Reference: 

van Rossum, G., Warsaw, B., & Coghlan, A. (2001). PEP 8: Style Guide for Python Code. Python Enhancement Proposals. Retrieved from https://peps.python.org/pep-0008/ (accessed 7th January 2026). 


 
