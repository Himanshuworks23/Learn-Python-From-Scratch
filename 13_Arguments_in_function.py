"""
Learning to use positional and keyword arguments in a function.
"""


def greet(first_name, last_name):
    print(f"Hi... {first_name} {last_name}")


greet("Himanshu", "Chawardol")  # Positional Argument

greet(last_name="Chawardol", first_name="Himanshu")  # Keyword Argument

print("Welcome Back!!...")
