# Modules
#   - Reusing the code
#         - Same Project
#         - Other Projects
#         - Other Globally
#  - Decompose the code

# 2 ways Modules
#     -Default Modules (Python Library)
#     -Custom Modules

"""
import math

print(math.floor(3.6))
print(math.ceil(3.6))
print(math.trunc(3.6))

# 3! = 3 * 2 * 1 = 6
# 5! = 5 * 4 * 3 * 2 * 1 = 120

print(math.factorial(3))
print(math.factorial(5))

"""


"""
import math, sys

for name in dir(sys):
    print(name)

print("Before Exit Statement")
sys.exit()

print("After Exit Statement")
"""

"""
import platform

print(platform.architecture())
print(platform.system())
print(platform.python_version())
print(platform.uname())
"""

"""
from random import random, choice, sample
from sys import exit

print(random())

numbers = [1, 2, 3, 4, 5, 6]
skills = ["DevOps", "AWS", "Python", "AI", "MLOps"]

print(choice(numbers))
print(sample(skills, 1))


def exit():
    print('I want Exit')


print("Before Exit Statement")
exit()
print("After Exit Statement")
"""