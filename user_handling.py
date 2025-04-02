# Jonas Fairchild, login and new user creation code -----------------------------------------------

def log_in(users): # Login function
    if users: # If there are users to log in as
        while True:
            print('Who do you want to log in as?: ')
            for user in users: # Get who the user wants to log in as
                print(f"- {user['name']}")
            login = input().lower()
            for user in users: # If the user they select exists
                if login == user['name'].lower():
                    while True: # Get them to enter the password
                        password = input("What is the password?: ")
                        if password == user['password']: # Returns the user's info
                            return user
                        print("That password is not correct. Try again.")
            print("That's not a user. Try again.")
    print("There are no users to log in as.")

def create_user(users): # Creates new users with their specifictions
    name = input("What do you want your account name to be?: ")
    password = input("What do you want your password to be?: ")
    balance = input("What do you want your account's initial balance to be?: ")
    users.append({'name': name, 'password': password, 'balance': balance, 'record': []}) # Adds the user to the list of users
    return users

# End of Jonas' code ------------------------------------------------------------------------------