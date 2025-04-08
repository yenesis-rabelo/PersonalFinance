
from entries import *
import datetime

def budgeting(user_info):

    today = datetime.date.today()
    end_year = today.year
    end_month = today.month
    end_day = today.day

    start_year = end_year
    start_month = end_month - 1
    start_day = end_day

    entries = copy.deepcopy(user_info['record'])
    entries.sort(key=sort_entries)
	
    for entry in entries[::-1]:
        if entry['date'][2] < start_year or (entry['date'][2] == start_year and entry['date'][0] < start_month) or (entry['date'][2] == start_year and entry['date'][0] == start_month and entry['date'][1] < start_day):
            entries.remove(entry)
        if entry['date'][2] > end_year or (entry['date'][2] == end_year and entry['date'][0] > end_month) or (entry['date'][2] == end_year and entry['date'][0] == end_month and entry['date'][1] > end_day):
            entries.remove(entry)
    
    total = 0
    for entry in entries:
        total += entry['amount']
    print(f"You've spent ${total} in the last month. This is your limit; all parts of your budget combined must not exceed this.")

    budget = []
    while True:
        location = input("Where is somewhere you spend your money? (shopping, gas, etc.): ").capitalize()
        amount = get_float("How much money per month will you allow yourself to spend there?: ")
        budget.append([amount, location])
        if input("Done adding categories? (Y/n): ").lower() == 'y':
            break

    budget_total = 0
    for i in budget:
        budget_total += i[0]
    print(f"Your budget uses ${budget_total} per month.")

    if total > budget_total:
        print("This means that your budget fits.\nYour budget:")
        for i in budget:
            print(f"\nCategory: {i[1]}\nMonthly amount: ${i[0]}\nPercent of monthly income: {i[0] / budget_total * 100}%")
    else:
        if input("Your budget does not fit. Would you like to try again? (Y/n)").lower() == 'y':
            budgeting(user_info)