"""
You received these records

records = [
    {
        "id": "1001",
        "name": " Laptop ",
        "city": "cairo",
        "price": "1200.50",
        "quantity": "2"
    },
    {
        "id": "1002",
        "name": "Mouse",
        "city": " GIZA ",
        "price": "450.00",
        "quantity": "3"
    },
    {
        "id": "1003",
        "name": " Keyboard ",
        "city": "alexandria",
        "price": "-150.00",
        "quantity": "2"
    },
    {
        "id": "1004",
        "name": "Monitor",
        "city": "cairo",
        "price": "800.00",
        "quantity": "0"
    }
]

Write a function: 
clean_record(record)

that returns a new cleaned dictionary.

For example:

clean_record(records[0])

should return:

{
    "id": 1001,
    "name": "Laptop",
    "city": "Cairo",
    "price": 1200.50,
    "quantity": 2
}

But now introduce validation.

Rules

A record is valid only if:

id > 0
price > 0
quantity > 0

If the record is invalid, your function should return:

None

Therefore:

clean_record(records[2])

should return:

None

because:

price = -150.00

And:

clean_record(records[3])

should also return:

None

because:

quantity = 0
"""
records = [
    {
        "id": "1001",
        "name": " Laptop ",
        "city": "cairo",
        "price": "1200.50",
        "quantity": "2"
    },
    {
        "id": "1002",
        "name": "Mouse",
        "city": " GIZA ",
        "price": "450.00",
        "quantity": "3"
    },
    {
        "id": "1003",
        "name": " Keyboard ",
        "city": "alexandria",
        "price": "-150.00",
        "quantity": "2"
    },
    {
        "id": "1004",
        "name": "Monitor",
        "city": "cairo",
        "price": "800.00",
        "quantity": "0"
    }
]

def clean_record(record):

    cleaned = {}
    
    for key, value in record.items():
        if key == 'id':
            try:    
                converted_id = int(value.strip())
                if converted_id > 0:
                    cleaned[key] = converted_id
                else:
                    return None 
            except ValueError:
                print("ValueError occured in id field")
                return None
        elif key == 'name':
            cleaned[key] = value.strip()
        elif key == 'city':
            cleaned[key] = value.strip().title()
        elif key == 'price':
            try:
                converted_price = float(value.strip())
                if converted_price > 0:
                    cleaned[key] = converted_price
                else:
                     return None
            except ValueError:
                print("ValueError occured in price field")    
                return None
        elif key == 'quantity':
            try:
                converted_quantity = int(value.strip())
                if converted_quantity > 0:
                    cleaned[key] = converted_quantity
                else:
                    return None
            except ValueError:
                print("ValueError occured in quantity field")
                return None
    # print(f"cleaned: {cleaned}, rejected: {rejected}")
    return cleaned            


rejected = []


for record in records:
    cleaned = clean_record(record)
    if cleaned is None:
        rejected.append(record)
    print(cleaned)

print("--------Rejected records--------")    
print(rejected)

original = records[0].copy()

clean_record(records[0])

assert records[0] == original    