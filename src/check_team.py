import pandas as pd

df = pd.read_csv("data/results.csv")

teams = sorted(
    set(df["home_team"]).union(
        set(df["away_team"])
    )
)

for team in teams:

    if "United" in team:
        print(team)

    if "Cura" in team:
        print(team)

    if "çao" in team:
        print(team)