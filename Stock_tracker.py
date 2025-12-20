# Simple Stock Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

total_investment = 0
details = []

print("Available Stocks:", stock_prices)

while True:
    stock = input("Enter stock name: ").upper()

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter quantity: "))
    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment
    details.append(f"{stock} | Qty: {quantity} | Value: {investment}")

    choice = input("Add another stock? (yes/no): ")
    if choice.lower() != "yes":
        break

print("\nTotal Investment Value:", total_investment)

# Save to investment_summary.txt
with open("investment_summary.txt", "w") as file:
    file.write("Stock Investment Summary\n")
    file.write("------------------------\n")
    for line in details:
        file.write(line + "\n")
    file.write(f"\nTotal Investment: {total_investment}")

print("investment_summary.txt file created successfully!")
