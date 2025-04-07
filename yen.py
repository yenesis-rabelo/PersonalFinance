import csv

# Exchange rates with USD as the default base currency
exchange_rates = {
    "USD": 1.0,     # Base currency (USD)
    "EUR": 0.92,    # 1 USD = 0.92 EUR
    "GBP": 0.78,    # 1 USD = 0.78 GBP
    "CAD": 1.35,    # 1 USD = 1.35 CAD
    "AUD": 1.5,     # 1 USD = 1.5 AUD
    "JPY": 110.0,   # 1 USD = 110 JPY
    "INR": 75.0     # 1 USD = 75 INR
}

def load_users_from_csv(filename="users.csv"):
    """Load users' data from a CSV file."""
    users = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append({"name": row[0], "balance": float(row[1])})
    except FileNotFoundError:
        print(f"Error: {filename} not found. Starting with an empty user list.")
    return users

def save_users_to_csv(users, filename="users.csv"):
    """Save users' data back to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for user in users:
            writer.writerow([user["name"], user["balance"]])

def convert_money(amount, from_currency, to_currency):
    """Converts an amount of money from one currency to another."""
    if from_currency == "USD":
        # Convert directly from USD to the target currency
        exchange_rate = exchange_rates.get(to_currency)
        if exchange_rate:
            return amount * exchange_rate
        else:
            return "Currency not supported."
    else:
        # If the base currency is not USD, convert to USD first, then to the target currency
        usd_amount = amount / exchange_rates.get(from_currency)
        exchange_rate = exchange_rates.get(to_currency)
        if exchange_rate:
            return usd_amount * exchange_rate
        else:
            return "Currency not supported."

def currency_converter(users):
    """Function to interact with the user, convert money, and update the users."""
    user_name = input("Enter your name: ")
    user_found = None

    # Load user data
    for user in users:
        if user["name"].lower() == user_name.lower():
            user_found = user
            break

    if not user_found:
        print(f"User {user_name} not found. Creating a new account.")
        user_found = {"name": user_name, "balance": 0.0}
        users.append(user_found)

    # User input for amount and currencies
    print(f"Current balance for {user_found['name']}: {user_found['balance']} USD")
    amount = float(input("Enter the amount of money you want to convert: "))
    from_currency = "USD"  # Default to USD for the user
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, GBP): ").upper()

    # Convert and display the result
    converted_amount = convert_money(amount, from_currency, to_currency)

    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")
        # Update the user's balance after conversion
        user_found["balance"] += amount  # Adding the converted amount to their balance
        save_users_to_csv(users)  # Save the updated users data to CSV
    else:
        print(converted_amount)  # Error message if currency is not supported

# Example of loading users, running currency converter, and saving data
users = load_users_from_csv()
currency_converter(users)
#code
