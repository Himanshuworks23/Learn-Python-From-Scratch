"""
Taking list of numbers and counting the average of numbers.

"""

numbers = [10, 20, 30, 40, 50]

total = 0
count = 0

for number in numbers:
    total += number
    count += 1

average = total / count
print("The average of the numbers is:", average)