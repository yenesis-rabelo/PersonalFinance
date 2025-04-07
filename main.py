#main menu testing function can be deleted

from budget import *
from saving import *


# Main Menu to choose the function(only for testing) must be intregrated to main 
def main():
    while True:
        print("\nMain Menu:")
        print("1. Set a Budget")
        print("2. View Last Entered Budget")
        print("3. Track Savings Goal")
        print("4. Exit")
        choice = input("Enter your choice: ")


        if choice == '1':
            budget()
        elif choice == '2':
            load_last_budget()
        elif choice == '3':
            savings_goal_tracker()
        elif choice == '4':
            break
        else:
            print("Please select a number 1-4")


if __name__ == "__main__":
    main()

