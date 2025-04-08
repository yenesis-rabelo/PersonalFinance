# Yenesis Rabelo, currency conversion ---------------------------------------------------------------------------------

import csv
from entries import get_float

def convert_money(amount, from_currency, to_currency):
    exchange_rates = {
    "USD": 1.0,     # Base currency (USD)
    "EUR": 0.92,    # 1 USD = 0.92 EUR
    "GBP": 0.78,    # 1 USD = 0.78 GBP
    "CAD": 1.35,    # 1 USD = 1.35 CAD
    "AUD": 1.5,     # 1 USD = 1.5 AUD
    "JPY": 110.0,   # 1 USD = 110 JPY
    "INR": 75.0     # 1 USD = 75 INR
    } 
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

def currency_converter():
    """Function to interact with the user, convert money, and update the users."""
    exchange_rates = {
    "USD": 1.0,     # Base currency (USD)
    "EUR": 0.92,    # 1 USD = 0.92 EUR
    "GBP": 0.78,    # 1 USD = 0.78 GBP
    "CAD": 1.35,    # 1 USD = 1.35 CAD
    "AUD": 1.5,     # 1 USD = 1.5 AUD
    "JPY": 110.0,   # 1 USD = 110 JPY
    "INR": 75.0     # 1 USD = 75 INR
    } 

    # User input for amount and currencies
    amount = get_float("Enter the amount of money you want to convert: ")
    from_currency = "USD"  # Default to USD for the user

    while True:
        print("Enter the currency you want to convert to:\nOptions:")
        for currency in exchange_rates.keys():
            print(f'- {currency}')
        to_currency = input().upper()
        if to_currency in exchange_rates.keys():
            break
        print("That's not in the list of options. Try again.")

    # Convert and display the result
    converted_amount = convert_money(amount, from_currency, to_currency)

    if isinstance(converted_amount, float):
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")
    else:
        print(converted_amount)  # Error message if currency is not supported

# End of Yenesis' code ------------------------------------------------------------------------------------------------