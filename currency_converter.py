# Define the exchange rates
exchange_rates = {
    "USD": {
        "EUR": 0.82,
        "GBP": 0.72,
        "JPY": 106.89,
        "AUD": 1.28,
        "CAD": 1.26
    },
    "EUR": {
        "USD": 1.22,
        "GBP": 0.87,
        "JPY": 131.64,
        "AUD": 1.58,
        "CAD": 1.56
    },
    "GBP": {
        "USD": 1.39,
        "EUR": 1.15,
        "JPY": 151.23,
        "AUD": 1.82,
        "CAD": 1.79
    },
    "JPY": {
        "USD": 0.0094,
        "EUR": 0.0076,
        "GBP": 0.0066,
        "AUD": 0.011,
        "CAD": 0.011
    },
    "AUD": {
        "USD": 0.78,
        "EUR": 0.63,
        "GBP": 0.55,
        "JPY": 88.43,
        "CAD": 0.98
    },
    "CAD": {
        "USD": 0.79,
        "EUR": 0.64,
        "GBP": 0.56,
        "JPY": 87.88,
        "AUD": 1.02
    }
}

# Prompt the user for input
amount = float(input("Enter the amount to convert: "))
base_currency = input("Enter the base currency: ").upper()
target_currency = input("Enter the target currency: ").upper()

# Convert the currency and display the result
converted_amount = amount * exchange_rates[base_currency][target_currency]
print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}.")
