from collections import defaultdict

# write a function clean_record(record) that returns 
# {
#     "id": 101,
#     "name": "Laptop",
#     "city": "Cairo",
#     "price": 1200.50,
#     "quantity": 2
# }
# Requirements:

# convert numeric fields
# strip whitespace from name
# normalize city
# return None if numeric conversion fails
# drill 1
record = {
    "id": "101",
    "name": " Laptop ",
    "city": " cairo ",
    "price": "1200.50",
    "quantity": "2"
}

def clean_record(record):
    try:
        new_record = {
            "id": int(record["id"]),
            "name": record["name"].strip(),
            "city": record["city"].strip().capitalize(),
            "price": float(record["price"]),
            "quantity": int(record["quantity"])
        }
        return new_record
    except (ValueError, KeyError):
        return None

print(clean_record(record))


##-------------------------------
# drill 2
records = [
    {"id": 1, "city": "Cairo", "price": 1200},
    {"id": 2, "city": "Giza", "price": 450},
    {"id": 3, "city": "Cairo", "price": 750},
    {"id": 4, "city": "Alexandria", "price": 1800},
    {"id": 5, "city": "Cairo", "price": 300},
]

prices_gt_700 = [record["id"] for record in records if record["price"] > 700]

print(prices_gt_700)

##-------------------------------
# drill 3
records = [
    {"id": 101, "name": "Laptop"},
    {"id": 102, "name": "Mouse"},
    {"id": 101, "name": "Laptop"},
    {"id": 103, "name": "Keyboard"},
    {"id": 102, "name": "Mouse"},
]

seen_ids = set()
recurrent_ids = set()

for record in records:
    if record["id"] in seen_ids:
        recurrent_ids.add(record["id"])
    else:
        seen_ids.add(record["id"])

print("ids appear more than one: ", list(recurrent_ids))

##-------------------------------
# drill 4

orders = [
    {"customer_id": 1, "amount": 500},
    {"customer_id": 2, "amount": 750},
    {"customer_id": 1, "amount": 300},
    {"customer_id": 3, "amount": 1200},
    {"customer_id": 2, "amount": 250},
]

total_amounts = defaultdict(int)

for order in orders:
    total_amounts[order["customer_id"]] += order["amount"]

print(dict(total_amounts))

# drill 5
list_of_orders = defaultdict(list)
for order in orders:
    list_of_orders[order["customer_id"]].append(order["amount"])

print(dict(list_of_orders))

##-------------------------------
# drill 6

customers = [
    {
        "id": 1,
        "name": "Ahmed",
        "orders": [
            {"id": 101, "amount": 500},
            {"id": 103, "amount": 300}
        ]
    },
    {
        "id": 2,
        "name": "Mona",
        "orders": [
            {"id": 102, "amount": 750}
        ]
    }
]

order_ids = []
for customer in customers:
    for order in customer["orders"]:
        order_ids.append(order["id"])

print(order_ids)
