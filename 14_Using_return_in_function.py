def add_numbers(num1, num2):
    result = num1 + num2
    return result


sum_result = add_numbers(11, 22)  # Function operation on integer function

print(f"The sum is: {sum_result}")


def concating(str1, str2):
    result = str1 + str2
    return result.upper()


concated_str = concating("Hello ", "World")   # Function operation on string function

print(f"The string after concatenating is {concated_str}. ")
