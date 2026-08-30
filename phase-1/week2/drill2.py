records = [
    {"id": 1, "name": "Laptop", "city": "Cairo", "price": 1200},
    {"id": 2, "name": "Mouse", "city": "Giza", "price": 450},
    {"id": 3, "name": "Keyboard", "city": "Cairo", "price": 750},
    {"id": 4, "name": "Monitor", "city": "Alexandria", "price": 1800},
    {"id": 5, "name": "Headset", "city": "Giza", "price": 300},
]

# products names
products =[ record["name"] for record in records]
print(products)

cairo_records = [record for record in records if record["city"] =='Cairo']
print(cairo_records)


expensive_ids = [record["id"] for record in records if record["price"] > 700]
print(expensive_ids)

city_names = {record["city"] for record in records}
print(city_names)


new_dict = [{ "name" :record["name"] , "price" : record["price"] } for record in records]
print(new_dict)