import csv

savings_file = "Financial_thing/savings_progress.csv"#must be changed to actual file path 


#load all existing saving goals 
def load_all_savings():
    savings = {}
    try:
        with open(savings_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                savings[name] = {
                    'goal': float(row['Goal']),
                    'saved': float(row['Saved'])
                }
    except FileNotFoundError:
        pass
    return savings

#saving all existing savings 
def save_all_savings(savings_dict):
    with open(savings_file, 'w', newline='') as file:
        fieldnames = ['Name', 'Goal', 'Saved', 'Remaining']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, data in savings_dict.items():
            goal = data['goal']
            saved = data['saved']
            remaining = goal - saved
            writer.writerow({
                'Name': name,
                'Goal': goal,
                'Saved': saved,
                'Remaining': remaining
            })


#displays all existing goals 
def display_all_goals(savings):
    print("\nCurrent Savings Goals:")
    if not savings:
        print("No goals found")
    else:
        for name, data in savings.items():
            goal = data['goal']
            saved = data['saved']
            print(f"- {name}: ${saved} / ${goal} ({round((saved / goal) * 100, 2)}%)")


#display the progress on a goal 
def display_progress(name, saved, goal):
    print(f"Progress on '{name}': ${saved} / ${goal} ({round((saved / goal) * 100, 2)}%)")


#function for taking the name of a goal 
def get_goal_name():
    return input("\nEnter the name of the goal to add to or create: ").strip()


#function to take amount for a goal
def new_goal_amount(name):
    while True:
        try:
            return float(input(f"Enter your savings goal for '{name}': $"))
        except ValueError:
            print("Please enter a valid number (anything above 0)")


#function to take savings amount 
def get_savings_amount():
    while True:
        try:
            amount = float(input("Enter amount to add (or 0 to stop): $"))
            if amount < 0:
                print("Amount cannot be negative")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number")


#function for tracking goals 
def savings_goal_tracker():
    savings = load_all_savings()
    display_all_goals(savings)

    name = get_goal_name()

    if name in savings:
        print(f"Updating existing goal '{name}'.")
        goal = savings[name]['goal']
        saved = savings[name]['saved']
    else:
        goal = new_goal_amount(name)
        saved = 0.0

    while True:
        amount = get_savings_amount()
        if amount == 0:
            break

        saved += amount
        savings[name] = {'goal': goal, 'saved': saved}
        save_all_savings(savings)

        if saved >= goal:
            print(f"Congrats you reached your goal '{name}' of ${goal}!")
            break
        else:
            display_progress(name, saved, goal)
