def add_income_entries():
	day = int(input("What is the day you got the money?"))
	month = int(input("What is the month you got the money"))
	year = int(input("What is the year you got the money"))
	income_date = [day, month, year]
	amount = int(input("How much money did you get?"))
	source = input("Where did you get it from?")
	income_entry = [income_date, amount, source]
def add_expense_entries():
	day = int(input("What is the day you used the money?"))
	month = int(input("What is the month you used the money"))
	year = int(input("What is the year you used the money"))
	expense_date = [day, month, year]
	amount = int(input("How much money did you use?"))
	category = input("What did you use it on? (rent, food, transportation, savings)")
	if category in ["rent", "food", "transportation", "savings"]: # adding more later (maybe?)
		expense_entry = [expense_date, amount, category]
	else:
		print("You didnt't enter a correct category!")
		return
		
def view_income_and_expenses():
	print("This is going to take the start date")
	day = int(input("What is the day of the month you want to start viewing stuff?"))
	month = int(input("What is the month of the year you want to start viewing stuff"))
	year = int(input("What is the year of the time you want to start viewing stuff?"))
	start_date = [day, month, year]
	print("This is going to take the end date")
	day = int(input("What is the day of the month you want to stop viewing stuff?"))
	month = int(input("What is the month of the year you want to stop viewing stuff"))
	year = int(input("What is the year of the time you want to stop viewing stuff?"))
	End_date = [day, month, year]
	#Find the first entry in records that is after the start date and select every entry up until the entry right before the end date
	#Print all of those entries
