import requests


def get_team_data(team_name):

    response = requests.get(
        "https://www.thesportsdb.com/api/v1/json/123/searchteams.php",
        params={
            "t": team_name
        }
    )

    data = response.json()

    if data["teams"] is None:
        return None

    team = data["teams"][0]

    return {
        "team": team["strTeam"],
        "country": team["strCountry"],
        "league": team["strLeague"],
        "stadium": team["strStadium"],
        "founded": team["intFormedYear"]
    }


if __name__ == "__main__":

    team_data = get_team_data(
        "Argentina"
    )

    print(team_data)