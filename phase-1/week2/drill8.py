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

# Drill 8 — Nested data + comprehensions
# Extract information from nested structures using comprehensions.
# Drill 8 — Task 1: Extract all order IDs

order_ids = [order["order_id"] for customer in customers for order in customer["orders"]]
print(order_ids)

#Task 2 — Filter nested data

# Now create a list containing the order IDs of orders whose amount is greater than 500.
order_ids_grester_than_500 = [order["order_id"] for customer in customers for order in customer["orders"] if order["amount"] > 500]
print(order_ids_grester_than_500)

# Task 3 — Extract customer/order pairs

# Create a list containing tuples like:

# [
#     (1, 101),
#     (1, 103),
#     (2, 102),
#     (2, 105),
#     (3, 104)
# ]

# Each tuple should contain:

# (customer_id, order_id)

# This combines:

# nested iteration
# tuple creation
# list comprehension

customer_order_tuples = [(customer["customer_id"], order["order_id"]) for customer in customers for order in customer["orders"] ]
print(customer_order_tuples)