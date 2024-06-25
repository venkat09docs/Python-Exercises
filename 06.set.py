# Set Data Type

"""
Defining List: []
Defining Tuple: ()
Defining Set: {}
"""

"""
        0     1     2     3      4
data = {10, 10.5, True, "RNS", "Tech"}
print(type(data))
print(data)
"""

"""
data = {10, 10.5, True, "RNS", "Tech"}
print(len(data))
print(data)

data = {10, 10.5, True, "RNS", "Tech", 10, True}
print(len(data))
print(data)

data = [10, 10.5, True, "RNS", "Tech", 10, True]
print(len(data))
print(data)
"""

"""
data = {10, 10.5, True, "RNS", "Tech"}

data[2] = 1000 # error stmt
print(data)
"""

"""
# Adding and removing items
data = {10, 10.5, True, "RNS", "Tech"}

data.add(1000)
data.remove(True)

print(data)
"""

"""
data = {10, 10.5, True, "RNS", "Tech"}
for item in data:
    print(item)
"""

"""
my_list = [1, 3, 5, 1, 9, 5, 1]
my_list = list(set(my_list))

print(my_list)
for item in my_list:
    print(item)
"""
