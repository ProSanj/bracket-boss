import requests

response = requests.get(
    "https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=Argentina"
)

data = response.json()

team = data["teams"][0]

print()
print("TEAM:", team["strTeam"])
print("COUNTRY:", team["strCountry"])
print("LEAGUE:", team["strLeague"])
print("STADIUM:", team["strStadium"])
print("FOUNDED:", team["intFormedYear"])
print("WEBSITE:", team["strWebsite"])