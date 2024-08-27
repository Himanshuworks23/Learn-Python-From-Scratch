"""By default, any input is stored as string hence it should be type-casted to desired data type"""

Birth_year=input("Enter your Birth year: ")

Age = 2024-int(Birth_year)

print(f"Age is: {Age}\n The variable age is of the type{type(Age)} ")

"""
Similar types of datatypes that can be explicitly type-casted are:
int()      integer
float()    float
bool()     boolean   
str()      string
"""