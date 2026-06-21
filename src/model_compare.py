import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier


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
        "away_goal_diff"
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

# Logistic Regression

lr_model = LogisticRegression(
    max_iter=1000
)

lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)

# Decision Tree

dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

dt_predictions = dt_model.predict(X_test)

dt_accuracy = accuracy_score(
    y_test,
    dt_predictions
)

# Random Forest

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

print()
print("Model Comparison")
print()

print("Logistic Regression:", lr_accuracy)

print("Decision Tree:", dt_accuracy)

print("Random Forest:", rf_accuracy)