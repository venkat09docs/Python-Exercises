# a function is a block of code which only runs when it is called

"""
return_val = print("Hello, How are you, Welcome")

print(return_val)
"""

"""
msg = "Welcome to Python Functions"
len_msg = len(msg)
print(len_msg)
"""

# greet() // error

"""
def greet():
    print("Hello, How are you")
    print("Welcome to Python Functions")
    print("!!!!!")


greet()

greet()

greet()
"""

"""
def get_average(input_numbers):
    sum_of_numbers = 0

    for num in input_numbers:
        sum_of_numbers += num
    avg = sum_of_numbers / len(input_numbers)
    print(avg)


my_list = [4, 8, 10, 20]
input_numbers = [1, 3, 5, 6]

get_average(my_list)

get_average(input_numbers)

get_average([1])
"""

"""
# Positional Based Args
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter = counter + 1
    print("Number of time", letter, " is ", str(counter))


print_letter_count("Welcome", "e")

print_letter_count("e", "Welcome")
"""

"""
# Parameters with Name
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter = counter + 1
    print("Number of time", letter, " is ", str(counter))


print_letter_count("Welcome", "e")

print_letter_count(letter="e", text="Welcome")
"""

"""
# Parameter with default values
def print_letter_count(letter, text="Welcome"):
    counter = 0
    for char in text:
        if char == letter:
            counter = counter + 1
    print("Number of time", letter, " is ", str(counter))


print_letter_count('e')
print_letter_count('t', "Welcome to Python Functions")
"""

"""
result = sum((1, 2, 3))
print(result)
"""

# Static based positional Args
"""
def mysum(a, b, c, d):
    print(a + b + c + d)

mysum(1, 2, 3, 4)

mysum(1, 2, 3, 4)
"""

"""
# Dynamic Args
def mysum(*args):
    print(sum(args))

mysum()

mysum(1, 2, 3, 4)

mysum(1, 2, 3, 4, 5, 10, 20, 30)
"""

"""
# Key word Based Args

def key_values_func(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs["name"])


key_values_func(name="Rnstech", salary=20000, age=12, address="Hyd")
"""