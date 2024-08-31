"""
Learning Dictionaries in Python.
"""

customers = {
    "id": 101,
    "name": "Himanshu",
    "phone": "9588620637",
    "premium": True
}

print(customers)
choice = input("What do you want from the dictionary: ").lower()

print(customers[choice])