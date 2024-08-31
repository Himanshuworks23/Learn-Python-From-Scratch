"""
Program to understand Lists
"""

names = ["Alex", "Brian", "Chevy", "David"]  # Initialization of list

print(names)  # Printing all the elements.

print(f"First element in the list is {names[0]}")  # Printing 1st element

print(f"First element in the list is {names[-1]}")  # Printing last element

# Performing append and pop operations
names.append("Elf")  # Adding new element at the end
print(names)  # Printing all the elements to check.

names.pop(0)  # Removing element at the index 0
print(names)  # Printing all the elements to check.

print(f"Number of elements in the list are: {len(names)}")  # Using len function to count number of elements in the List.