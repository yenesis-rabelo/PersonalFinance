# Matthew McKinley, income/expense tracking ---------------------------------------------------------------------------

import os
import copy

def get_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except:
			print("Invalid input. Try again.")

def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except:
			print("Invalid input. Try again.")

def sort_entries(entry):
	date = entry['date']
	return date[2] + (date[0] / 100) + (date[1] / 10000)
			
def add_income_entries(user_info):
	year = get_int("What is the year you got the money?: ")
	month = get_int("What is the month you got the money?: ")
	day = get_int("What is the day you got the money?: ")
	income_date = [month, day, year]

	amount = get_float("How much money did you get?: ")
	print("Where did you get it from?")
	if user_info['record']:
		print("Previously inputted categories (You can input things you haven't previously inputted):")
	locations = []
	for entry in user_info["record"]:
		if entry["location"] not in locations and entry['amount'] > 0:
			locations.append(entry["location"])
			print(f"- {entry['location']}")
	source = input().capitalize()
	income_entry = {'date': income_date, 'amount': amount, 'location': source}

	user_info["record"].append(income_entry)
	user_info['balance'] += amount
	return user_info

def add_expense_entries(user_info):
	year = get_int("What is the year you spent the money?: ")
	month = get_int("What is the month you spent the money?: ")
	day = get_int("What is the day you spent the money?: ")
	expense_date = [month, day, year]

	amount = -1 * get_float("How much money did you use?: ")
	print("What did you use it on?")
	if user_info['record']:
		print("Previously spent categories (You can input things you haven't previously inputted):")
	locations = []
	for entry in user_info["record"]:
		if entry["location"] not in locations and entry['amount'] < 0:
			locations.append(entry["location"])
			print(f"- {entry['location']}")
	source = input().capitalize()
	expense_entry = {'date': expense_date, 'amount': amount, 'location': source}

	user_info["record"].append(expense_entry)
	user_info['balance'] += amount
	return user_info
		
def view_income_and_expenses(user_info):

	start_year = get_int("\nWhat is the year of the time you want to start viewing entries?: ")
	start_month = get_int("What is the month of the year you want to start viewing entries?: ")
	start_day = get_int("What is the day of the month you want to start viewing entries?: ")

	end_year = get_int("\nWhat is the year of the time you want to stop viewing entries?: ")
	end_month = get_int("What is the month of the year you want to stop viewing entries?: ")
	end_day = get_int("What is the day of the month you want to stop viewing entries?: ")

	entries = copy.deepcopy(user_info['record'])
	entries.sort(key=sort_entries)

	for entry in entries[::-1]:
		if entry['date'][2] < start_year or (entry['date'][2] == start_year and entry['date'][0] < start_month) or (entry['date'][2] == start_year and entry['date'][0] == start_month and entry['date'][1] < start_day):
			entries.remove(entry)
		if entry['date'][2] > end_year or (entry['date'][2] == end_year and entry['date'][0] > end_month) or (entry['date'][2] == end_year and entry['date'][0] == end_month and entry['date'][1] > end_day):
			entries.remove(entry)
		
	for entry in entries:
		print(f"\nDate: {entry['date'][0]}/{entry['date'][1]}/{entry['date'][2]}\nAmount: ${entry['amount']}\nObtaining/spending location: {entry['location']}")


def income_expense_tracking(user_info):
	while True:
		os.system('cls')
		match input("What do you want to do?:\n1: Add income entries\n2: Add expense entries\n3: View entries for a specific time period\n4: View user balance\n5: Exit\n"):
			case '1':
				user_info = add_income_entries(user_info)
			case '2':
				user_info = add_expense_entries(user_info)
			case '3':
				view_income_and_expenses(user_info)
			case '4':
				print(f"Your balance is ${user_info['balance']}.")
			case '5':
				return user_info
			case _:
				print("Invalid input. Try again.")
		input("Done reading?: ")

# End of Matthew's code -----------------------------------------------------------------------------------------------