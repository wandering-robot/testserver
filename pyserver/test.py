import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":2, "name":"vide1", "views":17},
        {"likes":4, "name":"vide2", "views":21},
        {"likes":8, "name":"vide3", "views":36}
]

for i in range(len(data)):
    response = requests.put(BASE + f"video/{i}", data[i])
    print(response.json())

print("**********************")

response = requests.get(BASE + "video/7")
print(response.json())

