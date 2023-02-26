import json

# Load the exchange rates from the JSON file
with open("exchange_rates.json", "r") as f:
    exchange_rates = json.load(f)

# Prompt the user for input
amount = float(input("Enter the amount to convert: "))
base_currency = input("Enter the base currency: ").upper()
target_currency = input("Enter the target currency: ").upper()

# Convert the currency and display the result
converted_amount = amount * exchange_rates[base_currency][target_currency]
print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.")
