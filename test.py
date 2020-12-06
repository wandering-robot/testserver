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
