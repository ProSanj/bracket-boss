import pandas as pd
import joblib

from xgboost import XGBClassifier

# Load dataset

df = pd.read_csv("data/ml_dataset.csv")

# Features

X = df[
    [
        "home_form",
        "away_form",

        "home_win_rate",
        "away_win_rate",

        "home_scored_avg",
        "away_scored_avg",

        "home_conceded_avg",
        "away_conceded_avg",

        "home_goal_diff",
        "away_goal_diff",

        "home_elo",
        "away_elo",

        "elo_diff",
        "form_diff",
        "goal_diff_diff",

        "home_fifa_rank",
        "away_fifa_rank",
        "rank_diff"
    ]
]

# Target

y = df["result"]

# Convert labels to numbers

label_map = {
    "Away Win": 0,
    "Draw": 1,
    "Home Win": 2
}

y = y.map(label_map)

# Train model

model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    objective="multi:softprob",
    num_class=3,
    random_state=42
)

model.fit(X, y)

# Feature importance

for feature, importance in zip(
    X.columns,
    model.feature_importances_
):
    print(
        feature,
        round(float(importance), 4)
    )

# Save model

joblib.dump(
    model,
    "models/world_cup_model.pkl"
)

print("Model saved!")