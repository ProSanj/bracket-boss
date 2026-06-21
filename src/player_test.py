import requests

response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/123/searchplayers.php",
    params={
        "p": "Lionel Messi"
    }
)

print("STATUS:", response.status_code)
print()
print(response.text[:1000])