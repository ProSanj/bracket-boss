import requests

response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/123/searchplayers.php",
    params={
        "t": "Inter Miami"
    }
)

print(response.status_code)
print(response.text[:2000])