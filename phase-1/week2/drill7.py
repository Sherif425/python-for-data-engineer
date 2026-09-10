customers = [
    {
        "customer_id": 1,
        "name": "Ahmed",
        "orders": [
            {"order_id": 101, "amount": 500},
            {"order_id": 103, "amount": 300}
        ]
    },
    {
        "customer_id": 2,
        "name": "Mona",
        "orders": [
            {"order_id": 102, "amount": 750},
            {"order_id": 105, "amount": 250}
        ]
    },
    {
        "customer_id": 3,
        "name": "Omar",
        "orders": [
            {"order_id": 104, "amount": 1200}
        ]
    }
]

# Drill 7 — Task 1

# Write a loop that prints every customer's name.

# for customer in customers:
#     print(customer["name"])

# Task 2 — Access the nested orders

# Modify your loop so that for each customer you print their name and each order ID.    

for customer in customers:
    print(customer["name"])
    for order in customer["orders"]:
        print("  Order: " , order["order_id"])


# Task 3 — Calculate each customer's total

for customer in customers:
    total_amount = 0
    for order in customer["orders"]:
        total_amount += order["amount"]
    print(f"Customer: {customer['name']}, Total: {total_amount}")
    