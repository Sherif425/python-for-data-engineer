# Drill 12: Dictionary Methods
# Task 1:
customer_totals = {
    1: 800,
    2: 1000,
    3: 1200
}

for id in customer_totals:
    print(id)

for total in customer_totals.values():
    print(total)

for id, total in customer_totals.items():
    print("Customer", id, "->",  total)


# Task 2 — Find customers with high totals
greater_than_900 = []
for id, total in customer_totals.items():
    if total > 900:
        greater_than_900.append(id)

print(greater_than_900)

greater_than_900 = [id for id in customer_totals if customer_totals[id] > 900]
print(greater_than_900)