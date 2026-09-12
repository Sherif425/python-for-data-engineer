# Week 2 — Drill 11: Membership Testing

# Membership testing answers a very common data-processing question:

# "Does this value exist in this collection?"

customer_ids = [101, 102, 103, 104, 105]

print(103 in customer_ids)
print(999 in customer_ids)

# Task 2
customer_id_list = [101, 102, 103, 104, 105]
customer_id_set = {101, 102, 103, 104, 105}

print(103 in customer_id_list)
print(103 in customer_id_set)


# Task 3 Dictionary membership testing
customer_lookup = {
    1: "Ahmed",
    2: "Mona",
    3: "Omar"
}

print(1 in customer_lookup)
print("Ahmed" in customer_lookup.values())
