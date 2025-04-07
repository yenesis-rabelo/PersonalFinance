import csv


filename="Battle Simulator/yes/budget_data.csv" #change to actual file path


# Function to load the last entered budget
def load_last_budget():
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1:
                print("\nLast Budget Entry:")
                for line in data[1:]:
                    print(f"Category: {line[0]}, Amount: ${line[1]}")
            else:
                print("No budget found")
    except FileNotFoundError:
        print("No budget found")
       
# Function to save budget data to CSV
def save_budget_data(categories, income):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Amount'])
        for category, percentage in categories.items():
            amount = income * (percentage / 100)
            writer.writerow([category, round(amount, 2)])
        other = income - sum(income * (p / 100) for p in categories.values())
        writer.writerow(['Other', round(other, 2)])





#function to find the toal essentially takes user input and saves it 
def budget():
    income = float(input("Enter your total income: $"))
    categories = {
        "Savings": float(input("How much do you save annually (enter as percentage)? ")),
        "Entertainment": float(input("How much do you spend on entertainment (enter as percentage)? ")),
        "Transportation": float(input("How much do you spend on transportation (enter as percentage)? ")),
        "Utilities": float(input("How much do you spend on utilities (enter as percentage)? ")),
        "Food": float(input("How much do you spend on food (enter as percentage)? "))
    }


    total_percentage = sum(categories.values())


    if total_percentage > 100:
        print("Your percentage is over 100% please make sure it does not exceed 100%")
        return budget()


    print("\nBudget Breakdown:")
    for category, percentage in categories.items():
        amount = income * (percentage / 100)
        print(f"{category}: ${round(amount, 2)}")
   
    other = income - sum(income * (p / 100) for p in categories.values())
    print(f"Other: ${round(other, 2)}")
   
    # Save the budget data to CSV
    save_budget_data(categories, income)




if __name__ == "__main__":
    budget()
    load_last_budget()
    load_last_budget()
