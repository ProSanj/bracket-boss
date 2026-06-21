import pandas as pd

df = pd.read_csv("data/results.csv")

df = df.dropna(subset=["home_score", "away_score"])

team_stats = {}

for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    if home not in team_stats:
        team_stats[home] = {"wins": 0, "games": 0}

    if away not in team_stats:
        team_stats[away] = {"wins": 0, "games": 0}

    team_stats[home]["games"] += 1
    team_stats[away]["games"] += 1

    if row["home_score"] > row["away_score"]:
        team_stats[home]["wins"] += 1

    elif row["away_score"] > row["home_score"]:
        team_stats[away]["wins"] += 1

for team in ["Brazil", "Argentina", "France", "England"]:

    if team in team_stats:
        wins = team_stats[team]["wins"]
        games = team_stats[team]["games"]

        print(team)
        print("Games:", games)
        print("Wins:", wins)
        print("Win Rate:", round(wins / games, 3))
        print()