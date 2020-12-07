import requests

BASE = "http://127.0.0.1:5000/"


response = requests.post(BASE + "evanCompany/2/0",
                         {"userName": "John Smith", "userSolution": "Be better"})
print(response.json())

response = requests.post(BASE + "evanCompany/2/1",
                         {"userName": "Jane Smith", "userSolution": "Be better"})
print(response.json())

response = requests.post(BASE + "evanCompany/2/1",
                         {"userName": "Jerry Smith", "userSolution": "Be better"})
print(response.json())

response = requests.post(BASE + "evanCompany/2/1",
                         {"userName": "Bob Smith", "userSolution": "Be better"})
print(response.json())

response = requests.get(BASE + "evanCompany/2")
print(response.json())
