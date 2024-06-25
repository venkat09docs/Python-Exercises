# List Data Type

# List is Mutable

"""
# index    0    1     2                3
data =    [10, 10.5, True, "Welcome to Python Charm Editor"]
print(data[1])
"""

"""
data = [10, 10.5, True, "Welcome to Python Charm Editor"]
print(len(data))
data.append('Single quoted line')
print(data)
print(len(data))
"""

"""
data = [10, 10.5, True, "Welcome to Python Charm Editor"]
print(data)
data.insert(2, 20)
print(data)
data[3] = 200
data.append('Single quoted line')
print(data)
"""

"""
data = [10, 10.5, True, "Welcome to Python Charm Editor"]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])
"""

"""
data = [10, 10.5, True, "Welcome to Python Charm Editor", 20]
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
"""

"""
data = [10, 10.5, True, "Welcome to Python Charm Editor", 20, False]
print(len(data))
# element = 10
# element = 10.5
for element in data[::-1]:
    print(element)
"""

"""
# print 3rd and 4th element only
data = [10, 10.5, True, "Welcome to Python Charm Editor", 20, False]
for element in data[2:4:]:
    print(element)
"""

"""
# delete an element from the list
data = [10, 10.5, True, "Welcome to Python Charm Editor", 20, False]
del data[3]
print(data)
"""