import pandas as pd
from fifa_rankings import get_fifa_rank

df = pd.read_csv(
    "data/results.csv",
    encoding="latin1"
)

df = df.dropna(subset=["home_score", "away_score"])

team_form = {}
team_scored = {}
team_conceded = {}
team_elo = {}

home_forms = []
away_forms = []

home_scored_avg = []
away_scored_avg = []

home_conceded_avg = []
away_conceded_avg = []

home_win_rates = []
away_win_rates = []

home_elos = []
away_elos = []
home_fifa_ranks = []
away_fifa_ranks = []

rank_diffs = []

results = []

for _, row in df.iterrows():

    home = row["home_team"]
    away = row["away_team"]

    if home not in team_form:
        team_form[home] = []

    if away not in team_form:
        team_form[away] = []

    if home not in team_scored:
        team_scored[home] = []

    if away not in team_scored:
        team_scored[away] = []

    if home not in team_conceded:
        team_conceded[home] = []

    if away not in team_conceded:
        team_conceded[away] = []

    if home not in team_elo:
        team_elo[home] = 1500

    if away not in team_elo:
        team_elo[away] = 1500

    # FORM

    if len(team_form[home]) == 0:
        home_form = 0.5
    else:
        points = (
            team_form[home].count("W") * 3
            + team_form[home].count("D")
        )

        home_form = points / (
            len(team_form[home]) * 3
        )

    if len(team_form[away]) == 0:
        away_form = 0.5
    else:
        points = (
            team_form[away].count("W") * 3
            + team_form[away].count("D")
        )

        away_form = points / (
            len(team_form[away]) * 3
        )

    # GOALS SCORED

    if len(team_scored[home]) == 0:
        home_scored = 0
    else:
        home_scored = (
            sum(team_scored[home])
            / len(team_scored[home])
        )

    if len(team_scored[away]) == 0:
        away_scored = 0
    else:
        away_scored = (
            sum(team_scored[away])
            / len(team_scored[away])
        )

    # GOALS CONCEDED

    if len(team_conceded[home]) == 0:
        home_concede = 0
    else:
        home_concede = (
            sum(team_conceded[home])
            / len(team_conceded[home])
        )

    if len(team_conceded[away]) == 0:
        away_concede = 0
    else:
        away_concede = (
            sum(team_conceded[away])
            / len(team_conceded[away])
        )

    # WIN RATE

    if len(team_form[home]) == 0:
        home_win_rate = 0.5
    else:
        home_win_rate = (
            team_form[home].count("W")
            / len(team_form[home])
        )

    if len(team_form[away]) == 0:
        away_win_rate = 0.5
    else:
        away_win_rate = (
            team_form[away].count("W")
            / len(team_form[away])
        )

    # ELO FEATURES

    home_elo = team_elo[home]
    away_elo = team_elo[away]
    home_rank = get_fifa_rank(home)
    away_rank = get_fifa_rank(away)

    rank_diff = (
    away_rank
    - home_rank
)

    # SAVE FEATURES

    home_forms.append(home_form)
    away_forms.append(away_form)

    home_win_rates.append(home_win_rate)
    away_win_rates.append(away_win_rate)

    home_scored_avg.append(home_scored)
    away_scored_avg.append(away_scored)

    home_conceded_avg.append(home_concede)
    away_conceded_avg.append(away_concede)

    home_elos.append(home_elo)
    away_elos.append(away_elo)
    home_fifa_ranks.append(
    home_rank
)

    away_fifa_ranks.append(
    away_rank
)

    rank_diffs.append(
    rank_diff
)

    # TARGET

    if row["home_score"] > row["away_score"]:

        results.append("Home Win")

        team_form[home].append("W")
        team_form[away].append("L")

        actual_home = 1
        actual_away = 0

    elif row["home_score"] < row["away_score"]:

        results.append("Away Win")

        team_form[home].append("L")
        team_form[away].append("W")

        actual_home = 0
        actual_away = 1

    else:

        results.append("Draw")

        team_form[home].append("D")
        team_form[away].append("D")

        actual_home = 0.5
        actual_away = 0.5

    # ELO UPDATE

    K = 20

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

    team_elo[home] = (
        home_elo
        + K * (
            actual_home
            - expected_home
        )
    )

    team_elo[away] = (
        away_elo
        + K * (
            actual_away
            - expected_away
        )
    )

    # UPDATE HISTORY

    team_scored[home].append(
        row["home_score"]
    )

    team_scored[away].append(
        row["away_score"]
    )

    team_conceded[home].append(
        row["away_score"]
    )

    team_conceded[away].append(
        row["home_score"]
    )

    # KEEP LAST 5

    for team in [home, away]:

        if len(team_form[team]) > 5:
            team_form[team].pop(0)

        if len(team_scored[team]) > 5:
            team_scored[team].pop(0)

        if len(team_conceded[team]) > 5:
            team_conceded[team].pop(0)

feature_df = pd.DataFrame({
    "home_form": home_forms,
    "away_form": away_forms,

    "home_win_rate": home_win_rates,
    "away_win_rate": away_win_rates,

    "home_scored_avg": home_scored_avg,
    "away_scored_avg": away_scored_avg,

    "home_conceded_avg": home_conceded_avg,
    "away_conceded_avg": away_conceded_avg,

    "home_goal_diff": [
        scored - conceded
        for scored, conceded in zip(
            home_scored_avg,
            home_conceded_avg
        )
    ],

    "away_goal_diff": [
        scored - conceded
        for scored, conceded in zip(
            away_scored_avg,
            away_conceded_avg
        )
    ],

    "home_elo": home_elos,
    "away_elo": away_elos,
    "home_fifa_rank":
        home_fifa_ranks,

    "away_fifa_rank":
        away_fifa_ranks,

"rank_diff":
    rank_diffs,
    "elo_diff": [
    home - away
    for home, away in zip(
        home_elos,
        away_elos
    )
],

"form_diff": [
    home - away
    for home, away in zip(
        home_forms,
        away_forms
    )
],

"goal_diff_diff": [
    home - away
    for home, away in zip(
        [
            scored - conceded
            for scored, conceded in zip(
                home_scored_avg,
                home_conceded_avg
            )
        ],
        [
            scored - conceded
            for scored, conceded in zip(
                away_scored_avg,
                away_conceded_avg
            )
        ]
    )
],
    "result": results
})

print(feature_df.head())

print()
print("Rows:", len(feature_df))

feature_df.to_csv(
    "data/ml_dataset.csv",
    index=False
)

print("Dataset saved!")

print()
print("TOP ELO TEAMS")
print()

top_teams = sorted(
    team_elo.items(),
    key=lambda x: x[1],
    reverse=True
)

print()
print("Rows:", len(feature_df))
print("Dataset saved!")