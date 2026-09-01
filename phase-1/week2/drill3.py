records = [
    {"id": 1, "name": "Laptop", "city": "Cairo", "price": 1200},
    {"id": 2, "name": "Mouse", "city": "Giza"},
    {"id": 3, "name": "Keyboard", "city": "Cairo", "price": 750},
    {"id": 4, "name": "Monitor", "city": "Alexandria", "price": 1800},
]

# Task 1

# Write a loop that prints the price of every record.
# But if the price is missing, print:
# Price not available
# Don't allow the program to crash.

for record in records:
    try:
        if record["price"] is not None:
            print(record["price"])
    except KeyError:
        print("Price not available")

# Task 2

# Create a list containing the prices of all records.
# For a missing price, use:
# 0
# Expected:
# [1200, 0, 750, 1800]

prices = [record.get("price", 0) for record in records]
print("Prices", prices)

products=[record.get("name", 0) for record in records]
print(products)