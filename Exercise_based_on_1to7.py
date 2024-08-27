"""
Your task is to create a simple age checker for a roller coaster ride in Python,
The program should ask the user to enter their age.
Based on their age, provide different messages:
    If the user is between 18 and 45 years old(inclusive),
    print "Enjoy the ride!"

    If the user is under 18 years old,
    print"You're too young for this ride.

    If the user is over 45 years old,
    print "You're too old for this ride."
"""


Age = int(input("Enter your age: "))

if 18 < Age < 45:
    print("Enjoy the Ride!!...")

elif Age < 18:
    print("You are too young for this ride.")

elif Age > 45:
    print("You are too old for this ride.")

else:
    print("Invalid output.")

