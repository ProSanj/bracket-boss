import requests

response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/123/searchplayers.php",
    params={
        "p": "Lionel Messi"
    }
)

data = response.json()

player = data["player"][0]

print()
print("PLAYER FIELDS")
print("-" * 50)

for key in sorted(player.keys()):
    print(key)