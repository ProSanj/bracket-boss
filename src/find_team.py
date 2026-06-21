import pandas as pd

df = pd.read_csv("data/results.csv")

teams = set(df["home_team"]).union(
    set(df["away_team"])
)

for team in sorted(teams):

    if "Czech" in team:

        print(team)