
from entries import get_float
import datetime

def savings(user_info):
    date = datetime.date.today()
    if not user_info['goal']:
        user_info['goal'] = get_float("How much money do you want to have by the end of the month?: ")
        if user_info['goal'] < user_info['balance']:
            print("You already have more than that amount of money!")
            user_info['goal'] = None
            return savings(user_info)
        
    if user_info['goal'] < user_info['balance']:
        print("Congrats! You achieved your goal!")
    else:
        print(f"You have ${user_info['balance']}, which means ${user_info['goal'] - user_info['balance']} left to save, and {30 - date.day} days left to do it.\nTo save money, use the income/expense tracker to add an income entry.")

    if input("Do you want to make a new savings goal? (THIS WILL OVERRIDE YOUR PREVIOUS GOAL) (Y/n): ").lower() == 'y':
        while True:
            user_info['goal'] = get_float("How much money do you want to have by the end of the month?: ")
            if user_info['goal'] < user_info['balance']:
                print("You already have more than that amount of money!")
                user_info['goal'] = None
            else:
                break

        if user_info['goal'] < user_info['balance']:
            print("Congrats! You achieved your goal!")
        else:
            print(f"You have ${user_info['balance']}, which means ${user_info['goal'] - user_info['balance']} left to save, and {30 - date.day} days left to do it.\nTo save money, use the income/expense tracker to add an income entry.")