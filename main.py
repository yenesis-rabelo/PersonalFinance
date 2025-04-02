import os

def main(user_info, users):
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

def log_in(users):
    if users:
        print('Who do you want to log in as?: ')
        while True:
            for user in users:
                print(f"- {user['name']}")
            login = input().lower()
            for user in users:
                if login == user['name'].lower():
                    while True:
                        password = input("What is the password?: ")
                        if password == user['password']:
                            return user
                        print("That password is not correct. Try again.")
            print("That's not a user. Try again.")
    print("There are no users to log in as.")

def pre_main(users):
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
