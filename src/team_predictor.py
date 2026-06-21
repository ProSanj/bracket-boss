import pandas as pd

from sklearn.linear_model import LogisticRegression
df = pd.read_csv("data/results.csv")

df = df.dropna(subset=["home_score", "away_score"])
ml_df = pd.read_csv("data/ml_dataset.csv")

print("Dataset shape:", ml_df.shape)
print(ml_df.head())

X = ml_df[
    [
        "home_form",
        "away_form",
        "home_scored_avg",
        "away_scored_avg",
        "home_conceded_avg",
        "away_conceded_avg"
    ]
]

y = ml_df["result"]

model = LogisticRegression(
    max_iter=1000
)

model.fit(X, y)

home_team = input("Enter home team: ")

away_team = input("Enter away team: ")

def get_team_stats(team_name):

    matches = df[
        (df["home_team"] == team_name)
        | (df["away_team"] == team_name)
    ]

    recent_matches = matches.tail(5)

    wins = 0
    draws = 0

    goals_scored = []
    goals_conceded = []

    for _, row in recent_matches.iterrows():

        if row["home_team"] == team_name:

            scored = row["home_score"]
            conceded = row["away_score"]

            if scored > conceded:
                wins += 1
            elif scored == conceded:
                draws += 1

        else:

            scored = row["away_score"]
            conceded = row["home_score"]

            if scored > conceded:
                wins += 1
            elif scored == conceded:
                draws += 1

        goals_scored.append(scored)
        goals_conceded.append(conceded)

    points = wins * 3 + draws

    if len(recent_matches) == 0:
        form = 0.5
    else:
        form = points / (len(recent_matches) * 3)

    avg_scored = sum(goals_scored) / len(goals_scored)
    avg_conceded = sum(goals_conceded) / len(goals_conceded)

    return form, avg_scored, avg_conceded


home_form, home_scored, home_conceded = get_team_stats(home_team)

away_form, away_scored, away_conceded = get_team_stats(away_team)

match = pd.DataFrame([
    {
        "home_form": home_form,
        "away_form": away_form,
        "home_scored_avg": home_scored,
        "away_scored_avg": away_scored,
        "home_conceded_avg": home_conceded,
        "away_conceded_avg": away_conceded
    }
])

prediction = model.predict(match)

probabilities = model.predict_proba(match)

print()
print(home_team, "vs", away_team)

print()
print("Prediction:")
print(prediction[0])

print()

for outcome, probability in zip(
    model.classes_,
    probabilities[0]
):
    print(
        outcome,
        ":",
        round(probability * 100, 2),
        "%"
    )