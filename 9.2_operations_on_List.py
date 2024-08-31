"""
Create a program that prompts the user to enter 5 numbers.
Calculate the squares of each number and store them in separate lists.
Allow the user to choose either the original numbers list or the squares list.
Prompt the user to enter an index number.
Retrieve and display the element at the specified index from the chosen list.
"""

numbers = []
squares = []
for n in range(5):
    temp = int(input(f"Enter the number for index position {n}: "))
    numbers.append(temp)
    squares.append((temp * temp))

print(f"The entered list is: {numbers} \nAnd the squares are: {squares} ")

list_name = (input("Enter the name of list you want value from: ")).lower().strip()
if (list_name == "numbers") or (list_name == "squares"):
    i = int(input("Enter the index number you want value from: ").strip())
    if i <= len(numbers) if list_name == "numbers" else len(squares):

        if list_name == "numbers":
            print(f"The item at the index number {i} in the list {list_name} is: {numbers[i]}")
        else:
            print(f"The item at the index number {i} in the list {list_name} is: {squares[i]}")
    else:
        print("Invalid Input")
else:
    print("Invalid input")
