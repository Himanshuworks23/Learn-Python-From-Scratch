"""
Creating list of dictionaries
"""

customers = [
    {
        "id": 101,
        "name": "Himanshu",
        "DOB": "23-04-1999",
        "premium": True
    },
{
        "id": 102,
        "name": "Rahul",
        "DOB": "29-01-2001",
        "premium": False
    },
{
        "id": 103,
        "name": "Mohit",
        "DOB": "06-12-2004",
        "premium": True
    }
]
for customer in customers:
    print(customer["id"])
    print(customer["name"])
    print(customer["DOB"])
    print(customer["premium"])
    print("_______________________________")