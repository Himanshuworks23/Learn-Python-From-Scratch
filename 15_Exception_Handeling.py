"""
Example of Try Except Block.
"""
print("Give me 2 numbers, and I will divide them.\n Press x to exit ")
while True:
    p = (input("Enter Numerator value: "))
    if p == "x":
        break
    q = (input("Enter Denominator value: "))

    try:
        result = float(p) / float(q)
        print(result)

    except ZeroDivisionError:
        print("Denominator cannot be zero")

# Jar try madhe error ali tar ch toh except block madhe jayil. Manun jya operation madhe error yeu shakte toh try block madhech karaycha...
