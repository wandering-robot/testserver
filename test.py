import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld")
print(response.json())

response = requests.get(BASE + "evanCompany")
print(response.json())

print('\n')

response = requests.get(BASE + "evanCompany/2")
print(response.json())

print('\n')

response = requests.get(BASE + "evanCompany/2/4")
print(response.json())

print('\n')

response = requests.put(BASE + "evanCompany/2/4",
                        {"userName": "John Smith", "userSolution": "Be better"})
print(response.json())

response = requests.put(BASE + "evanCompany/2",
                        {"problemId": 2})
print(response.json())

response = requests.put(BASE + "evanCompany/",
                        {"problem": "you all suck"})
print(response.json())
