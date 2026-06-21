from predictor import get_team_elo

teams = [
    "Qatar",
    "Argentina",
    "France",
    "Brazil",
    "England",
    "Spain",
    "Morocco"
]

for team in teams:
    print(
        team,
        get_team_elo(team)
    )