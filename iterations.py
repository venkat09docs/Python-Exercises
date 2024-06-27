# Iterations or Loops

"""
top_cities = ["Hyd", "Bngl", "Chennai", "Mumbai", "Delhi", "Pune"]

# print(top_cities[0])
# print(top_cities[1])
# print(top_cities[2])
# print(top_cities[3])
# print(top_cities[4])


# Syntax of for loop
for item in list:
    print(item)
print("Hello")


for city in top_cities:
    print(city)

"""

"""
greeting = "Hello! Welcome to RNS"

for char in greeting:
    print(char)
"""

"""
users = { "A": 20000, "B": 15000, "C": 30000 }

# print(users["A"])

for user in users:
    print(user)

for user in users:
    print(users[user])

for user in users.keys():
    print("User Name - " + user)

for sal in users.values():
    print("Salary - " + str(sal))

"""

"""
users = [("A", 20000, 25), ("B", 15000, 20), ("C", 30000)]

# print(len(users))

for (name, sal, age) in users:
    # print(type(user))
    # print(user)
    # print("User Name is - " + user[0])
    # print("User Sal is - " + str(user[1]))
    # print("User Age is - " + str(user[2]))
    print("User Name is - " + name)
    print("User Sal is - " + str(sal))
    print("User Age is - " + str(age))
    
"""

# while loop

# while condition:
    # while loop stmts

"""
data = 1
while data <= 10:
    print(data)
    data = data + 1
"""

# continue and Break stmts

"""
# Continue Statement
data = [1, 2, 0, 10, 15, 0, 25, 45, 0]

for item in data:
    if item == 0:
        continue
    else:
        print(item)

"""

"""
# break statement
data = [1, 2, 0, 10, 15, 0, 25, 45, 0]

item_found = False
search = 15
for item in data:
    if search == item:
        print("Hurray!!! Item is found")
        item_found = True
        break
if not(item_found):
    print("Item not found")
"""