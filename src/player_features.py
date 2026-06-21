import requests

url = (
    "https://www.thesportsdb.com/"
    "api/v1/json/123/searchplayers.php"
    "?t=Inter Miami"
)

response = requests.get(url)

print("STATUS:", response.status_code)

print()
print("FIRST 1000 CHARACTERS:")
print("-" * 40)

print(response.text[:1000])