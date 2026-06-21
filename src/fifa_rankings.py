FIFA_RANKINGS = {
    "Argentina": 1,
    "Spain": 2,
    "France": 3,
    "England": 4,
    "Brazil": 5,
    "Portugal": 6,
    "Netherlands": 7,
    "Belgium": 8,
    "Germany": 9,
    "Croatia": 10,
    "Morocco": 11,
    "Italy": 12,
    "Uruguay": 13,
    "Colombia": 14,
    "Japan": 15,
    "Mexico": 16,
    "United States": 17,
    "Iran": 18,
    "Senegal": 19,
    "South Korea": 20
}

def get_fifa_rank(team):
    return FIFA_RANKINGS.get(team, 100)