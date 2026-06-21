print("MONTE CARLO FILE STARTED")
import time
import random
import predictor
from predictor import predict_match


SIMULATIONS = 1000

groups = {
    "A": [
        "Mexico",
        "South Africa",
        "South Korea",
        "Czech Republic"
    ],

    "B": [
        "Canada",
        "Bosnia and Herzegovina",
        "Qatar",
        "Switzerland"
    ],

    "C": [
        "Brazil",
        "Morocco",
        "Haiti",
        "Scotland"
    ],

    "D": [
        "United States",
        "Paraguay",
        "Australia",
        "Turkey"
    ],

    "E": [
        "Germany",
        "Curaçao",
        "Ivory Coast",
        "Ecuador"
    ],

    "F": [
        "Netherlands",
        "Japan",
        "Sweden",
        "Tunisia"
    ],

    "G": [
        "Belgium",
        "Egypt",
        "Iran",
        "New Zealand"
    ],

    "H": [
        "Spain",
        "Cape Verde",
        "Saudi Arabia",
        "Uruguay"
    ],

    "I": [
        "France",
        "Senegal",
        "Iraq",
        "Norway"
    ],

    "J": [
        "Argentina",
        "Algeria",
        "Austria",
        "Jordan"
    ],

    "K": [
        "Portugal",
        "DR Congo",
        "Uzbekistan",
        "Colombia"
    ],

    "L": [
        "England",
        "Croatia",
        "Ghana",
        "Panama"
    ]
}
def simulate_group(group_teams):

    standings = {}

    for team in group_teams:

        standings[team] = {
            "points": 0,
            "wins": 0
        }

    for i in range(len(group_teams)):

        for j in range(i + 1, len(group_teams)):

            home = group_teams[i]
            away = group_teams[j]

            prediction, probs = predict_match(
                home,
                away
            )

            prediction = random.choices(
                [
                    "Away Win",
                    "Draw",
                    "Home Win"
                ],
                weights=probs,
                k=1
            )[0]

            if prediction == "Home Win":

                standings[home]["points"] += 3
                standings[home]["wins"] += 1

            elif prediction == "Away Win":

                standings[away]["points"] += 3
                standings[away]["wins"] += 1

            else:

                standings[home]["points"] += 1
                standings[away]["points"] += 1

    return sorted(
        standings.items(),
        key=lambda x: (
            x[1]["points"],
            x[1]["wins"]
        ),
        reverse=True
    )
def simulate_knockout_round(teams):

    winners = []

    for i in range(len(teams) // 2):

        home = teams[i]
        away = teams[-(i + 1)]

        prediction, probs = predict_match(
            home,
            away
        )

        prediction = random.choices(
            [
                "Away Win",
                "Home Win"
            ],
            weights=[
                probs[0],
                probs[2]
            ],
            k=1
        )[0]

        if prediction == "Away Win":

            winners.append(away)

        else:

            winners.append(home)

    return winners

def simulate_tournament():
    #print("Tournament started")
    group_winners = []
    group_runners_up = []
    third_place_teams = []

    for _, group_teams in groups.items():

        standings = simulate_group(
            group_teams
        )

        group_winners.append(
            standings[0][0]
        )

        group_runners_up.append(
            standings[1][0]
        )

        third_place_teams.append(
            standings[2]
        )

    third_place_teams = sorted(
        third_place_teams,
        key=lambda x: (
            x[1]["points"],
            x[1]["wins"]
        ),
        reverse=True
    )

    best_third_place = (
        third_place_teams[:8]
    )

    knockout_teams = []

    knockout_teams.extend(
        group_winners
    )

    knockout_teams.extend(
        group_runners_up
    )

    for team, _ in best_third_place:

        knockout_teams.append(
            team
        )

    round_of_32 = (
        simulate_knockout_round(
            knockout_teams
        )
    )

    round_of_16 = (
        simulate_knockout_round(
            round_of_32
        )
    )

    quarterfinals = (
        simulate_knockout_round(
            round_of_16
        )
    )

    semifinals = (
        simulate_knockout_round(
            quarterfinals
        )
    )

    home = semifinals[0]
    away = semifinals[1]

    prediction, probs = predict_match(
        home,
        away
    )

    prediction = random.choices(
        [
            "Away Win",
            "Home Win"
        ],
        weights=[
            probs[0],
            probs[2]
        ],
        k=1
    )[0]

    if prediction == "Away Win":

        champion = away

    else:

        champion = home

    return champion

print("Monte Carlo started")

champion_counts = {}

start = time.time()

for _ in range(SIMULATIONS):

    champion = (
        simulate_tournament()
    )

    champion_counts[champion] = (
        champion_counts.get(
            champion,
            0
        ) + 1
    )

end = time.time()

print()
print(
    "Runtime:",
    round(end - start, 2),
    "seconds"
)

print()
print("=" * 40)
print("WORLD CUP WINNING ODDS")
print("=" * 40)
print()

results = sorted(
    champion_counts.items(),
    key=lambda x: x[1],
    reverse=True
)

for team, wins in results:

    percentage = (
        wins / SIMULATIONS
    ) * 100

    print(
        f"{team}: "
        f"{percentage:.1f}% "
        f"({wins} wins)"
    )

print()
print(
    "Predictions:",
    predictor.prediction_counter
)