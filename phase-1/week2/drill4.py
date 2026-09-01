records = [
    {"id": 1001, "name": "Laptop", "city": "Cairo", "price": 1200},
    {"id": 1002, "name": "Mouse", "city": "Giza", "price": 450},
    {"id": 1003, "name": "Keyboard", "city": "Cairo", "price": 750},
    {"id": 1002, "name": "Mouse", "city": "Giza", "price": 450},
    {"id": 1004, "name": "Monitor", "city": "Alexandria", "price": 1800},
    {"id": 1003, "name": "Keyboard", "city": "Cairo", "price": 750},
]
# Task 1 — Find duplicate IDs
seen_ids = set()
duplicate_ids = set()
for record in records:
    record_id = record.get("id")
    if record_id in seen_ids:
        duplicate_ids.add(record_id)
    else:
        seen_ids.add(record_id)

print("Duplicate IDs:", duplicate_ids)
print(f"seen ids: {seen_ids}")


# Task 2 — Keep only unique records
# eate a new list containing only the first occurrence of each ID.
seen_ids = set()
record_unique = []
for record in records:
    record_id =record.get("id")
    if record_id not in seen_ids:
        seen_ids.add(record_id)
        record_unique.append(record)

print("Unique Records:", record_unique)


# Task 3 — Count occurrences

# Create a dictionary like:

# {
#     1001: 1,
#     1002: 2,
#     1003: 2,
#     1004: 1
# }
ocurrences = {}
for record in records:
    record_id = record.get("id")
    if record_id in ocurrences:
        ocurrences[record_id] += 1
    else:
        ocurrences[record_id] = 1
print("Occurrences:", ocurrences)
