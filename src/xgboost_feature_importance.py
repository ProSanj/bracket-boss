import pandas as pd
import joblib

model = joblib.load(
    "models/world_cup_model.pkl"
)

features = [
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
    "away_elo"
]

for feature, importance in zip(
    features,
    model.feature_importances_
):
    print(
        f"{feature}: "
        f"{importance:.4f}"
    )