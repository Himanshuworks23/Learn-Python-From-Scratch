"""
Program to understand Tuple &
Difference between tuple and list.
"""

# Syntax:

names = ("Himanshu", "Mohit", "Aditya", "Raj", "Yash")
# Syntax of Lists : names = ["Alex", "Brian", "Chevy", "David"]
# Difference is the brackets tuple => (), Lists => []
n = 0
for name in names:
    print(f"Name at {n} is: {names[n]}")
    n += 1

# Note: We cannot change/update tuple. Hence, operations like update or modify in any format cannot be done.
