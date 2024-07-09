"""

import json

emp = '{ "name": "RNS Tech", "age": 15, "salary": "2L" }'

data = json.loads(emp)

print(data["name"])
print(data["age"])
print(data["salary"])
"""
import json

"""
import requests, json

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
# print(response.json())

data = response.json()

for row in data:
    print(row["title"])
"""

import requests

"""
inputdata = {
                "title": "Rnstech",
                "userId": 1,
                "body": " Example Data "
            }

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=inputdata)

print(response.status_code)
print(response.json())
"""

"""
response = requests.delete("https://jsonplaceholder.typicode.com/posts1")

print(response.status_code)
print(response.json())
"""


import http.client

conn = http.client.HTTPSConnection("linkedin-data-api.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "b39ff4d59cmshf6d72b6eb6b1c8dp1ee645jsn51ab52903648",
    'x-rapidapi-host': "linkedin-data-api.p.rapidapi.com"
}

conn.request("GET", "/?username=gvenkat09", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

profile = json.loads(data)

print(profile["summary"])

# print(data.decode("utf-8"))
