records = [
    {"id": 1, "name": "Laptop", "city": "Cairo", "price": 1200},
    {"id": 2, "name": "Mouse", "city": "Giza", "price": 450},
    {"id": 3, "name": "Keyboard", "city": "Cairo", "price": 750},
    {"id": 4, "name": "Monitor", "city": "Alexandria", "price": 1800},
    {"id": 5, "name": "Headset", "city": "Giza", "price": 300},
]

# Write code to produce the following.

# Task 1 — Extract names

# Produce:

# ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset']
products = []
for record in records:
    products.append(record["name"])
print(products)    

# Task 2 — Filter by city

# Produce all records where:

# city == "Cairo"
all_cairo = []
for record in records:
    if record["city"] == "Cairo":
        all_cairo.append(record)
print(all_cairo)
# Expected:

# [
#     {"id": 1, "name": "Laptop", "city": "Cairo", "price": 1200},
#     {"id": 3, "name": "Keyboard", "city": "Cairo", "price": 750}
# ]
# Task 3 — Filter by price

# Produce all records where:

# price > 700

# Expected IDs:

# [1, 3, 4]
prices_over_700 = []
for record in records:
    if record["price"] > 700:
        prices_over_700.append(record["id"])
print(prices_over_700)


# Task 4 — Unique cities

# Produce:

# {"Cairo", "Giza", "Alexandria"}

unique_cities = set()
for record in records:
    unique_cities.add(record["city"])
print(unique_cities)

# The order of a set doesn't matter.

# Task 5 — Find a record

# Using the list, retrieve the name and price of the record with:

# id == 4
for record in records:
    if record["id"] == 4:
        print(record["name"])
        print(record["price"])


# Expected:

# Monitor
# 1800