# Jonas Fairchild, main and pre-main functions ----------------------------------------------------

import os
from user_handling import *
from file_handling import *

def main(user_info, users): # Main function that branches out to other parts of the program.
    while True:
        os.system('cls')
        match input('What do you want to do?\n1: Income/expense tracking\n2: Budgeting\n3: Goal Tracker\n4: Visualizations\n5: Convert currency\n6: Log out\n') :
            case '1':
                #income_expense_tracking()
                pass
            case '2':
                #budgeting()
                pass
            case '3':
                #goal_tracker()
                pass
            case '4':
                #visualizations()
                pass
            case '5':
                #convert_currency()
                pass
            case '6':
                return user_info
            case _:
                print("That's not a valid input. Try again.")
        input("Done reading?: ")

def pre_main(users): # Pre-main function for before the user logs in, lets the user create an account, log in, or stop the program.
    while True:
        os.system('cls')
        match input("What do you want to do?:\n1: Create new user\n2: Log in\n3: Exit\n"):
            case '1':
                users = create_user(users)
            case '2':
                user_info = log_in(users)
                if user_info:
                    user_info = main(user_info, users)
            case '3':
                return users
            case _:
                print("That's not a valid input. Try again.")
        input('Done reading?: ')

save(pre_main(load())) # Call the pre-main function by loading the users from the csv file, then save the result

# End of Jonas' code ------------------------------------------------------------------------------