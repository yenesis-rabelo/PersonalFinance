# Jonas Fairchild, main and pre-main functions ------------------------------------------------------------------------

run = True
import os
from user_handling import *
from file_handling import *
from entries import income_expense_tracking
from InquirerPy import inquirer

try:
    from pie_chart import pie_chart
except:
    print("It looks like you haven't installed matplotlib yet. To do this, type 'pip3 install matplotlib' into the terminal.")
    run = False
    
def main(user_info, users): # Main function that branches out to other parts of the program.
    while True:
        os.system('cls')
        action = inquirer.select( # Gets the user's choice using InquirerPy
            message =  "What do you want to do?",
            choices = [
                "Track income/expenses",
                "Use budgeting tool",
                "Track goals",
                "Visualize income/expense categories",
                "Convert currency",
                "Log out",
            ],
            default = None
        ).execute()

        match action: # Calls the appropriate function for the user's choice
            case "Track income/expenses":
                user_info = income_expense_tracking(user_info)
            case "Use budgeting tool":
                #budgeting()
                pass
            case "Track goals":
                #goal_tracker()
                pass
            case "Visualize income/expense categories":
                pie_chart(user_info)
            case "Convert currency":
                #convert_currency()
                pass
            case "Log out":
                return user_info
        input("Done reading?: ")

def pre_main(users): # Pre-main function for before the user logs in, lets the user create an account, log in, or stop the program.
    while True:
        os.system('cls')
        action = inquirer.select( # Gets the user's choice using InquirerPy
            message =  "What do you want to do?",
            choices = [
                "Create new user",
                "Log in",
                "Exit",
            ],
            default = None
        ).execute()

        match action: # Calls the appropriate function for the user's choice
            case "Create new user":
                users = create_user(users)
            case "Log in":
                user_info = log_in(users)
                if user_info:
                    user_info = main(user_info, users)
            case "Exit":
                return users
        input('Done reading?: ')

if run:
    save(pre_main(load())) # Calls the pre-main function by loading the users from the csv file, then save the result

# End of Jonas' code --------------------------------------------------------------------------------------------------