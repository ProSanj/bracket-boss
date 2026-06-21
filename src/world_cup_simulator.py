import random

from predictor import predict_match

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

            print(home, "vs", away)
            print(prediction)
            print()

            if prediction == "Home Win":

                standings[home]["points"] += 3
                standings[home]["wins"] += 1

            elif prediction == "Away Win":

                standings[away]["points"] += 3
                standings[away]["wins"] += 1

            else:

                standings[home]["points"] += 1
                standings[away]["points"] += 1

    sorted_table = sorted(
        standings.items(),
        key=lambda x: (
            x[1]["points"],
            x[1]["wins"]
        ),
        reverse=True
    )

    return sorted_table


group_winners = []
group_runners_up = []
third_place_teams = []

for group_name, group_teams in groups.items():

    print()
    print("=" * 40)
    print("GROUP", group_name)
    print("=" * 40)
    print()

    standings = simulate_group(group_teams)

    print("STANDINGS")
    print()

    for team, stats in standings:

        print(
            team,
            "-",
            stats["points"],
            "pts",
            "(",
            stats["wins"],
            "wins )"
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

    print()
    print(
        "Qualified:",
        standings[0][0],
        ",",
        standings[1][0]
    )

    print(
        "Third Place:",
        standings[2][0]
    )

third_place_teams = sorted(
    third_place_teams,
    key=lambda x: (
        x[1]["points"],
        x[1]["wins"]
    ),
    reverse=True
)

best_third_place = third_place_teams[:8]

knockout_teams = []

knockout_teams.extend(
    group_winners
)

knockout_teams.extend(
    group_runners_up
)

for team, stats in best_third_place:

    knockout_teams.append(team)

print()
print("=" * 40)
print("GROUP WINNERS")
print("=" * 40)

for team in group_winners:

    print(team)

print()
print("=" * 40)
print("RUNNERS-UP")
print("=" * 40)

for team in group_runners_up:

    print(team)

print()
print("=" * 40)
print("BEST THIRD PLACE TEAMS")
print("=" * 40)

for team, stats in best_third_place:

    print(
        team,
        "-",
        stats["points"],
        "pts",
        "(",
        stats["wins"],
        "wins )"
    )

print()
print("=" * 40)
print("ROUND OF 32 TEAMS")
print("=" * 40)

for team in knockout_teams:

    print(team)

print()
print(
    "TOTAL TEAMS:",
    len(knockout_teams)
)

print()
print("=" * 40)
print("KNOCKOUT STAGE")
print("=" * 40)


def simulate_knockout_round(
    teams,
    round_name
):

    print()
    print("=" * 40)
    print(round_name)
    print("=" * 40)
    print()

    winners = []

    for i in range(
        len(teams) // 2
    ):

        home = teams[i]

        away = teams[
            -(i + 1)
        ]

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

        print(
            home,
            "vs",
            away
        )

        if prediction == "Away Win":

            winner = away

        else:

            winner = home

        print(
            "Winner:",
            winner
        )

        print()

        winners.append(
            winner
        )

    return winners


round_of_32 = simulate_knockout_round(
    knockout_teams,
    "ROUND OF 32"
)

round_of_16 = simulate_knockout_round(
    round_of_32,
    "ROUND OF 16"
)

quarterfinals = simulate_knockout_round(
    round_of_16,
    "QUARTERFINALS"
)

semifinalists = simulate_knockout_round(
    quarterfinals,
    "SEMIFINALS"
)


print()
print("=" * 40)
print("FINAL")
print("=" * 40)
print()

home = semifinalists[0]
away = semifinalists[1]

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

print(
    home,
    "vs",
    away
)

if prediction == "Away Win":

    champion = away

else:

    champion = home

print()
print("=" * 40)
print("WORLD CUP CHAMPION")
print("=" * 40)
print()

print(
    "🏆",
    champion
)