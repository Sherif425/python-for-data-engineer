# Drill 6: Grouping with defaultdict(list)3
# Use this:

# orders = [
#     {"order_id": 101, "customer_id": 1, "amount": 500},
#     {"order_id": 102, "customer_id": 2, "amount": 750},
#     {"order_id": 103, "customer_id": 1, "amount": 300},
#     {"order_id": 104, "customer_id": 3, "amount": 1200},
#     {"order_id": 105, "customer_id": 2, "amount": 250},
# ]

# We want to build something conceptually like:

# {
#     1: [
#         {"order_id": 101, "customer_id": 1, "amount": 500},
#         {"order_id": 103, "customer_id": 1, "amount": 300}
#     ],
#     2: [
#         {"order_id": 102, "customer_id": 2, "amount": 750},
#         {"order_id": 105, "customer_id": 2, "amount": 250}
#     ],
#     3: [
#         {"order_id": 104, "customer_id": 3, "amount": 1200}
#     ]
# }

# Notice the difference:

# defaultdict(int)
# customer 1 → 800
# defaultdict(list)
# customer 1 → [order 101, order 103]

# So:

# defaultdict(int)   → aggregation
# defaultdict(list)  → grouping

# 2. The key mechanism

# Start with:

# from collections import defaultdict

# orders_by_customer = defaultdict(list)

# The interesting part is:

# defaultdict(list)

# When Python encounters a customer that doesn't exist yet:

# orders_by_customer[1]

# it automatically creates:

# orders_by_customer[1] = []

# Therefore we can immediately do:

# orders_by_customer[1].append(order)

# No .get() and no explicit:

# if customer_id not in orders_by_customer:
# Your Drill

# Write a loop that groups the orders by customer_id.

# Requirements

# Use:

# defaultdict(list)

# and .append().

# Do not use:

# .get()
# if customer_id not in ...
# comprehensions

# The essential operation should be:

# orders_by_customer[customer_id].append(order)

# Then print:

# print(orders_by_customer)

from collections import defaultdict

orders = [
    {"order_id": 101, "customer_id": 1, "amount": 500},
    {"order_id": 102, "customer_id": 2, "amount": 750},
    {"order_id": 103, "customer_id": 1, "amount": 300},
    {"order_id": 104, "customer_id": 3, "amount": 1200},
    {"order_id": 105, "customer_id": 2, "amount": 250},
]

orders_by_customer = defaultdict(list)

for order in orders:
    orders_by_customer[order["customer_id"]].append(order)

print(orders_by_customer)