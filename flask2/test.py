import requests

BASE = "http://127.0.0.1:5000/"

data = [ {"likes": 10, "name":"Dora the explorer", "views":10000},
         {"likes": 2123, "name":"Mobile Legends Tutorial", "views":14600},
         {"likes": 3213, "name":"Realme Note 8", "views":4626}
         ]

for i in range(len(data)):
    response = requests.put(BASE + "/video/" + str(i), data[i])
    print(response.json())

#input()
#response = requests.delete(BASE + "/video/0")
#print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())