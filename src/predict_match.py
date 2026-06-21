import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset

df = pd.read_csv("data/ml_dataset.csv")

X = df[
    [
        "home_form",
        "away_form",
        "home_scored_avg",
        "away_scored_avg",
        "home_conceded_avg",
        "away_conceded_avg"
    ]
]

y = df["result"]

# Train model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Example match

# Example match

match = pd.DataFrame([
    {
        "home_form": 0.10,
        "away_form": 0.90,
        "home_scored_avg": 0.5,
        "away_scored_avg": 3.0,
        "home_conceded_avg": 2.5,
        "away_conceded_avg": 0.5
    }
])

prediction = model.predict(match)

probabilities = model.predict_proba(match)

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