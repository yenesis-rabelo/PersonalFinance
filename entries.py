
def add_income_entries(user_info):
	day = int(input("What is the day you got the money?"))
	month = int(input("What is the month you got the money"))
	year = int(input("What is the year you got the money"))
	income_date = [day, month, year]
	amount = float(input("How much money did you get?"))
	source = input("Where did you get it from?")
	income_entry = [income_date, amount, source]
	user_info["record"].append(income_entry)
	return user_info

def add_expense_entries(user_info):
	day = int(input("What is the day you used the money?\n"))
	month = int(input("What is the month you used the money?\n"))
	year = int(input("What is the year you used the money?\n"))
	expense_date = [day, month, year]
	amount = float(input("How much money did you use?"))
	print("What did you use it on?\nPreviously spent categories (You can input things you haven't previously inputted)")
	locations = []
	for entry in user_info["record"]:
		entry["location"]
		if entry["location"] not in locations:
			locations.append(entry["location"])
			print(f"- {entry["location"]}")
	source = input().capitalize
	expense_entry = [expense_date, amount, source]
	user_info["record"].append(expense_entry)
	return user_info
		

def view_income_and_expenses():
	print("This is going to take the start date")
	day = int(input("What is the day of the month you want to start viewing stuff?\n"))
	month = int(input("What is the month of the year you want to start viewing stuff?\n"))
	year = int(input("What is the year of the time you want to start viewing stuff?\n"))
	start_date = [day, month, year]
	print("This is going to take the end date")
	day = int(input("What is the day of the month you want to stop viewing stuff?\n"))
	month = int(input("What is the month of the year you want to stop viewing stuff?\n"))
	year = int(input("What is the year of the time you want to stop viewing stuff?\n"))
	end_date = [day, month, year]
	#Find the first entry in records that is after the start date and select every entry up until the entry right before the end date
	#Print all of those entries