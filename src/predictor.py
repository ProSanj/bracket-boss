prediction_counter = 0
import pandas as pd
import joblib

# Load datasets

df = pd.read_csv("data/results.csv")

df = df.dropna(
    subset=["home_score", "away_score"]
)

# Load model

model = joblib.load(
    "models/world_cup_model.pkl"
)

# --------------------------
# CACHE
# --------------------------

team_stats_cache = {}
team_elo_cache = {}

# --------------------------
# TEAM STATS
# --------------------------

def get_team_stats(team_name):

    if team_name in team_stats_cache:
        return team_stats_cache[team_name]

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

        form = points / (
            len(recent_matches) * 3
        )

    if len(goals_scored) == 0:

        avg_scored = 0
        avg_conceded = 0

    else:

        avg_scored = (
            sum(goals_scored)
            / len(goals_scored)
        )

        avg_conceded = (
            sum(goals_conceded)
            / len(goals_conceded)
        )

    if len(recent_matches) == 0:

        win_rate = 0.5

    else:

        win_rate = (
            wins
            / len(recent_matches)
        )

    team_stats_cache[team_name] = (
        form,
        avg_scored,
        avg_conceded,
        win_rate
    )

    return team_stats_cache[team_name]


# --------------------------
# TEAM ELO
# --------------------------

def get_team_elo(team_name):

    if team_name in team_elo_cache:
        return team_elo_cache[team_name]

    elo_ratings = {}

    teams = set(df["home_team"]).union(
        set(df["away_team"])
    )

    for team in teams:
        elo_ratings[team] = 1500

    for _, row in df.iterrows():

        home = row["home_team"]
        away = row["away_team"]

        home_elo = elo_ratings[home]
        away_elo = elo_ratings[away]

        if row["home_score"] > row["away_score"]:

            actual_home = 1
            actual_away = 0

        elif row["home_score"] < row["away_score"]:

            actual_home = 0
            actual_away = 1

        else:

            actual_home = 0.5
            actual_away = 0.5

        expected_home = (
            1 /
            (
                1 +
                10 ** (
                    (away_elo - home_elo)
                    / 400
                )
            )
        )

        expected_away = (
            1 - expected_home
        )

        K = 20

        elo_ratings[home] = (
            home_elo
            + K * (
                actual_home
                - expected_home
            )
        )

        elo_ratings[away] = (
            away_elo
            + K * (
                actual_away
                - expected_away
            )
        )

    team_elo_cache[team_name] = (
        elo_ratings[team_name]
    )

    return team_elo_cache[team_name]

# --------------------------
# PREDICT MATCH
# --------------------------

def predict_match(
    home_team,
    away_team
):
    global prediction_counter

    prediction_counter += 1
    (
        home_form,
        home_scored,
        home_conceded,
        home_win_rate
    ) = get_team_stats(
        home_team
    )

    (
        away_form,
        away_scored,
        away_conceded,
        away_win_rate
    ) = get_team_stats(
        away_team
    )

    home_elo = get_team_elo(
        home_team
    )

    away_elo = get_team_elo(
        away_team
    )

    match = pd.DataFrame([
    {

        "home_form":
            home_form,

        "away_form":
            away_form,

        "home_win_rate":
            home_win_rate,

        "away_win_rate":
            away_win_rate,

        "home_scored_avg":
            home_scored,

        "away_scored_avg":
            away_scored,

        "home_conceded_avg":
            home_conceded,

        "away_conceded_avg":
            away_conceded,

        "home_goal_diff":
            home_scored
            - home_conceded,

        "away_goal_diff":
            away_scored
            - away_conceded,

        "home_elo":
            home_elo,

        "away_elo":
            away_elo,

        "elo_diff":
            home_elo
            - away_elo,

        "form_diff":
            home_form
            - away_form,

        "goal_diff_diff":
            (
                home_scored
                - home_conceded
            )
            -
            (
                away_scored
                - away_conceded
            ),

        "home_fifa_rank":
            50,

        "away_fifa_rank":
            50,

        "rank_diff":
            0
    }
])

    prediction_num = model.predict(
        match
    )[0]

    label_map = {
        0: "Away Win",
        1: "Draw",
        2: "Home Win"
    }

    prediction = label_map[
        prediction_num
    ]

    probabilities = (
        model.predict_proba(
            match
        )[0]
    )

    return (
        prediction,
        probabilities
    )

# --------------------------
# TEAM DASHBOARD
# --------------------------

def get_team_dashboard(team_name):

    (
        form,
        avg_scored,
        avg_conceded,
        win_rate
    ) = get_team_stats(
        team_name
    )

    elo = get_team_elo(
        team_name
    )

    return {

        "elo":
            round(
                elo,
                0
            ),

        "form":
            round(
                form,
                2
            ),

        "win_rate":
            round(
                win_rate * 100,
                1
            ),

        "goals_scored":
            round(
                avg_scored,
                2
            ),

        "goals_conceded":
            round(
                avg_conceded,
                2
            )
    }