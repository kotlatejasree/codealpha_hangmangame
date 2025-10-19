# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 135,
    "MSFT": 330
}

# Dictionary to hold user portfolio
portfolio = {}

# Get user input
print("Enter your stock portfolio.")
print("Type 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")
        continue

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares x ${price} = ${investment}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this portfolio to a file? (yes/no): ").lower()

if save == "yes":
    file_format = input("Choose format (txt/csv): ").lower()
    filename = f"portfolio.{file_format}"

    if file_format == "txt":
        with open(filename, "w") as file:
            file.write("Your Portfolio:\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            file.write(f"\nTotal Investment: ${total_investment}")
    elif file_format == "csv":
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                file.write(f"{stock},{qty},{price},{qty * price}\n")
            file.write(f",,,{total_investment}")
    else:
        print("Invalid format. File not saved.")
    print(f"Portfolio saved to {filename}")
