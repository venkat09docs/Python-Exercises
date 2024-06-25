# Dictionary Data Type

# Key = Value

# Name = Server
# env = dev

# {"us-east-1": ["us-east-1a", "us-east-1b", "us-east-1c"], "us-west-1": ["us-west-1a", "us-west-1b", "us-west-1c"]}

"""
data = {"Name": "Server", "env": "dev"}
print(type(data))
"""

"""
data = {"us-east-1": {"us-east-1a", "us-east-1b", "us-east-1c"},
        "us-west-1": ["us-west-1a", "us-west-1b", "us-west-1c"],
        "us-southeast-1": ("us-southeast-1a"),
        20: "Twenty"}

print(data)
print(data["us-west-1"])
print(type(data["us-west-1"]))

print(data[20])

print(data["us-southeast-1"])
for az in data["us-west-1"]:
    print("Availability Zone - " + az)
"""

"""
data = {"us-east-1": {"us-east-1a", "us-east-1b", "us-east-1c"},
        "us-west-1": ["us-west-1a", "us-west-1b", "us-west-1c"],
        "us-southeast-1": ("us-southeast-1a"),
        20: "Twenty"}

print(data.values())

for val in data.values():
    print(val)

print(data.keys())

for key in data.keys():
    print(key)
"""

"""
emp = { "name": "RNS Tech",
        "age": 12,
        "skills": ["AWS", "DevOps", "Python"],
        "salary": "2L"}

# Adding item in dict
emp["address"] = ["Flat", "Street", "City", "State", "PINCODE"]

# print(emp)
# print(emp["address"])

emp["age"] = 13
emp["skills"] = ["AWS", "DevOps", "Python", "Docker"]

for skill in emp["skills"]:
    print(skill)

# print(emp)

"""

"""
emp = { "name": "RNS Tech",
        "age": 12,
        "skills": {
                    "DevOps": ["Git", "Ansible", "Docker"], 
                    "Cloud": ["AWS", "Azure", "GCP"]},
        "salary": "2L"
      }

print(emp["skills"]['DevOps'])
"""