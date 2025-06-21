
 # Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()

    if stock == 'DONE':
        break

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity
    else:
        print("Invalid stock symbol. Try again.")

# Display result
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock}: {qty} shares x ${price} = ${qty * price}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Stock Portfolio:\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio saved to 'portfolio_summary.txt'")