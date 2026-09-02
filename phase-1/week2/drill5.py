orders = [
    {"order_id": 101, "customer_id": 1, "amount": 500},
    {"order_id": 102, "customer_id": 2, "amount": 750},
    {"order_id": 103, "customer_id": 1, "amount": 300},
    {"order_id": 104, "customer_id": 3, "amount": 1200},
]

customers = [
    {"customer_id": 1, "name": "Ahmed"},
    {"customer_id": 2, "name": "Mona"},
    {"customer_id": 3, "name": "Omar"},
]

# Task 1 — Build a customer lookup

# Transform:

# customers

# into:

# {
#     1: "Ahmed",
#     2: "Mona",
#     3: "Omar"
# }
customer_lookup = {customer["customer_id"]: customer["name"] for customer in customers}
print("Customer Lookup:", customer_lookup)
# Task 2 — Enrich the orders

# Create:

# enriched_orders

# containing:

# [
#     {"order_id": 101, "customer_id": 1, "customer_name": "Ahmed", "amount": 500},
#     {"order_id": 102, "customer_id": 2, "customer_name": "Mona", "amount": 750},
#     {"order_id": 103, "customer_id": 1, "customer_name": "Ahmed", "amount": 300},
#     {"order_id": 104, "customer_id": 3, "customer_name": "Omar", "amount": 1200}
# ]

enriched_orders = []
for order in orders:
    customer_id = order["customer_id"]
    customer_name = customer_lookup.get(customer_id, "Unknown")
    enriched_order = {
        "order_id": order["order_id"],
        "customer_id": customer_id,
        "customer_name": customer_name,
        "amount": order["amount"]
    }
    enriched_orders.append(enriched_order)

print("Enriched Orders:", enriched_orders)

for enriched_order in enriched_orders:
    print(f"Order ID: {enriched_order['order_id']}, Customer Name: {enriched_order['customer_name']}, Amount: {enriched_order['amount']}")


prices = {enriched_order["customer_id"]: enriched_order["amount"] for enriched_order in enriched_orders}
print("Prices:", prices)
total = {}

for enriched_order in enriched_orders:
    name = enriched_order["customer_name"]
    price = enriched_order["amount"]
    total[name] = total.get(name, 0) + price

    
print("Total:", total)


from collections import defaultdict

total_amounts = defaultdict(int)
total = {}
for enriched_order in enriched_orders:
    # id = enriched_order["customer_id"]
    # amount = enriched_order["amount"]
    # total_amounts[id] += amount
    total[name] = total.get(name, 0) + price

print("Total Amounts:", total)