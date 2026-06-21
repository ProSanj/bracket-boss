import pandas as pd
import time

start = time.time()

for _ in range(10000):

    match = pd.DataFrame([
        {
            "home_form": 0.6,
            "away_form": 0.4,

            "home_win_rate": 0.6,
            "away_win_rate": 0.4,

            "home_scored_avg": 2.0,
            "away_scored_avg": 1.2,

            "home_conceded_avg": 0.8,
            "away_conceded_avg": 1.4,

            "home_goal_diff": 1.2,
            "away_goal_diff": -0.2,

            "home_elo": 1900,
            "away_elo": 1800
        }
    ])

end = time.time()

print(
    "10000 DataFrames:",
    round(end - start, 2),
    "seconds"
)