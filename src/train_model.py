import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset

df = pd.read_csv("data/ml_dataset.csv")

# Features

X = df[
    [
        "home_form",
        "away_form",

        "home_scored_avg",
        "away_scored_avg",

        "home_conceded_avg",
        "away_conceded_avg",

        "home_goal_diff",
        "away_goal_diff",

        "home_elo",
        "away_elo"
    ]
]

# Target

y = df["result"]

# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict

predictions = model.predict(X_test)

# Accuracy

accuracy = accuracy_score(
    y_test,
    predictions
)

print("Accuracy:", accuracy)