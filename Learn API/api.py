import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {"id": 2}

response = requests.get(url, params=params)
print(response.url)

response.raise_for_status()

print("Status code", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

data = response.json()
print(data)