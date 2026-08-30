"""
Given 
record = {
    "id": "1001",
    "name": " Laptop ",
    "city": "cairo",
    "price": "1200.50",
    "quantity": "2"
}
Write Python code that produces:
{
    "id": 1001,
    "name": "Laptop",
    "city": "Cairo",
    "price": 1200.50,
    "quantity": 2
}
"""

record = {
    "id": "1001",
    "name": " Laptop ",
    "city": "cairo",
    "price": "1200.50",
    "quantity": "2"
}

new_record = {
    "id": int(record["id"]),
    "name": record["name"].strip(),
    "city": record["city"].title(),
    "price": float(record["price"]),
    "quantity": int(record["quantity"])
}