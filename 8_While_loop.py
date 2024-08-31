"""
Write a program to Calculate sum of numbers from 1 to n.
Take the input of n from the user.
"""
count = 0
sum = 0


print("Program to calculate sum of numbers upto n")

n = int(input("Give the value of n: "))

while count <= n:
    sum += count
    count += 1

print(f"Sum of numbers from 1 to {n} is = {sum}")

