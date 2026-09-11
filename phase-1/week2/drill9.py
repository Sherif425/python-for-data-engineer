# Tuples
# Task 1
# Given 
# customer_order = (1, 101)
# Use tiple unpacking to create two variables: customer_id and order_id. Then print them.

customer_order = (1, 101)
customer_id, order_id = customer_order

print("Customer:", customer_id, "Order:", order_id)


# Task 2
customer_orders = [
    (1, 101),
    (1, 103),
    (2, 102),
    (2, 105),
    (3, 104)
]

for customer_id, order_id in customer_orders:
    print("Customer:", customer_id, "->", "Order:", order_id)

# Task 3 — Dictionary unpacking with .items()
customer_totals = {
    1: 800,
    2: 1000,
    3: 1200
}

for customer_id , total in customer_totals.items():
    print("Customer:", customer_id, "->",  "Total:", total)


record = (101, "Laptop", 1200, "Cairo")
order_id, name, price, city = record
print("Order ID:", order_id)
print("Name:", name)
print("Price:", price)
print("City:", city)


record = (101, "Laptop", 1200, "Cairo", "Egypt")
order_id, *data, country = record
print("Order ID:", order_id)
print("Other Data:", data)
print("Country:", country)  
