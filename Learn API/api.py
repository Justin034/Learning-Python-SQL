import requests

url = "https://pokeapi.co/api/v2/pokemon"
params = {"offset": 0, "limit": 200}

response = requests.get(url, params=params)
print(response.url)

response.raise_for_status()

print("Status code", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

data = response.json()
print(data["count"])

print(data)
for x in data["results"]:
    print(x)
    test = requests.get(x["url"])
    test.raise_for_status()
    data2 = test.json()
    print(data2["stats"][0]["base_stat"])
    print()
    print()
    
