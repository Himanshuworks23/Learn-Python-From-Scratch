"""
Learning about parameterless and parameterised function.
"""

# Note Function Names should always be in lower case (not compulsory nut a standard practice)

name = input("Enter your name: ")


def greet():                                  # Parameterless Function initialization
    print(name)


print(f"Welcome to learning functions:")

greet()                                        # Function call


def greetings(name):
    print("Welcome back " + name)

greetings(name)


"""
def greetings(name):
    print("Welcome back " + name)

greetings("Mohit")
"""