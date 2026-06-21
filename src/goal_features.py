import pandas as pd

df = pd.read_csv("data/results.csv")
df = df.dropna(subset=["home_score", "away_score"])

team_scored = {}
team_conceded = {}

home_scored_avg = []
away_scored_avg = []

home_conceded_avg = []
away_conceded_avg = []

for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    if home not in team_scored:
        team_scored[home] = []

    if away not in team_scored:
        team_scored[away] = []

    if home not in team_conceded:
        team_conceded[home] = []

    if away not in team_conceded:
        team_conceded[away] = []

    if len(team_scored[home]) == 0:
        home_scored = 0
    else:
        home_scored = sum(team_scored[home]) / len(team_scored[home])

    if len(team_scored[away]) == 0:
        away_scored = 0
    else:
        away_scored = sum(team_scored[away]) / len(team_scored[away])

    if len(team_conceded[home]) == 0:
        home_concede = 0
    else:
        home_concede = sum(team_conceded[home]) / len(team_conceded[home])

    if len(team_conceded[away]) == 0:
        away_concede = 0
    else:
        away_concede = sum(team_conceded[away]) / len(team_conceded[away])

    home_scored_avg.append(home_scored)
    away_scored_avg.append(away_scored)

    home_conceded_avg.append(home_concede)
    away_conceded_avg.append(away_concede)

    team_scored[home].append(row["home_score"])
    team_scored[away].append(row["away_score"])

    team_conceded[home].append(row["away_score"])
    team_conceded[away].append(row["home_score"])

    if len(team_scored[home]) > 5:
        team_scored[home].pop(0)

    if len(team_scored[away]) > 5:
        team_scored[away].pop(0)

    if len(team_conceded[home]) > 5:
        team_conceded[home].pop(0)

    if len(team_conceded[away]) > 5:
        team_conceded[away].pop(0)

df["home_scored_avg"] = home_scored_avg
df["away_scored_avg"] = away_scored_avg

df["home_conceded_avg"] = home_conceded_avg
df["away_conceded_avg"] = away_conceded_avg

print(
    df[
        [
            "home_team",
            "away_team",
            "home_scored_avg",
            "away_scored_avg",
            "home_conceded_avg",
            "away_conceded_avg"
        ]
    ].head(20)
)