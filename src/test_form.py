import pandas as pd

# Load data
df = pd.read_csv("data/results.csv")

# Remove matches with missing scores
df = df.dropna(subset=["home_score", "away_score"])

# Keep track of recent results for every team
team_form = {}

# Store generated features
home_forms = []
away_forms = []

for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    # Create team entries if they don't exist
    if home not in team_form:
        team_form[home] = []

    if away not in team_form:
        team_form[away] = []

    # -----------------------------
    # Calculate home form score
    # -----------------------------
    home_results = team_form[home]

    if len(home_results) == 0:
        home_form = 0.5
    else:
        points = (
            home_results.count("W") * 3
            + home_results.count("D")
        )

        home_form = points / (len(home_results) * 3)

    # -----------------------------
    # Calculate away form score
    # -----------------------------
    away_results = team_form[away]

    if len(away_results) == 0:
        away_form = 0.5
    else:
        points = (
            away_results.count("W") * 3
            + away_results.count("D")
        )

        away_form = points / (len(away_results) * 3)

    home_forms.append(home_form)
    away_forms.append(away_form)

    # -----------------------------
    # Determine match result
    # -----------------------------
    if row["home_score"] > row["away_score"]:

        team_form[home].append("W")
        team_form[away].append("L")

    elif row["home_score"] < row["away_score"]:

        team_form[home].append("L")
        team_form[away].append("W")

    else:

        team_form[home].append("D")
        team_form[away].append("D")

    # Keep only last 5 matches
    if len(team_form[home]) > 5:
        team_form[home].pop(0)

    if len(team_form[away]) > 5:
        team_form[away].pop(0)

# Add features to dataframe
df["home_form"] = home_forms
df["away_form"] = away_forms

print(df[
    [
        "home_team",
        "away_team",
        "home_form",
        "away_form"
    ]
].head(20))