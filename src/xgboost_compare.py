import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier

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
        "away_elo"
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

# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------
# RANDOM FOREST
# --------------------------

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)

rf_predictions = rf_model.predict(
    X_test
)

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

# --------------------------
# XGBOOST
# --------------------------

xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    objective="multi:softmax",
    num_class=3,
    random_state=42
)

xgb_model.fit(
    X_train,
    y_train
)

xgb_predictions = xgb_model.predict(
    X_test
)

xgb_accuracy = accuracy_score(
    y_test,
    xgb_predictions
)

# --------------------------
# RESULTS
# --------------------------

print()
print("RANDOM FOREST ACCURACY")
print(round(rf_accuracy * 100, 2), "%")

print()
print("XGBOOST ACCURACY")
print(round(xgb_accuracy * 100, 2), "%")