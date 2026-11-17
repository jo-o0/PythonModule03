import random


achievements: list[str] = [
    "Headshot",
    "Master Coder",
    "PimPamPum!",
    "TrashLover",
    "Spoon Master",
    "Treelicious",
    "ChainSmoker",
    "Worker of the Month",
    "Screener"
]


def player_achievement() -> set:
    random_number: int = random.randint(1, len(achievements))
    random_achiev: list[str] = random.sample(achievements, random_number)
    return set(random_achiev)


if __name__ == "__main__":
    print(" === Achievement Tracker System ===\n")
    p1: set = player_achievement()
    p2: set = player_achievement()
    p3: set = player_achievement()
    p4: set = player_achievement()
    print(f"**Player 1 Achievements: {p1}\n")
    print(f"**Player 2 Achievements: {p2}\n")
    print(f"**Player 3 Achievements: {p3}\n")
    print(f"**Player 4 Achievements: {p4}\n")
    players: list = [p1, p2, p3, p4]
    all_achievements = p1.union(p2, p3, p4)
    print(f"**All Achievements**\n{all_achievements}\n")
    shared: set = set.intersection(p1, p2, p3, p4)
    print(f"**Shared Achievements**\n{shared}\n")
    i: int = 1
    for player in players:
        others: set = set().union(*[p for p in players if p is not player])
        exclusive_achiev: set = set.difference(player, others)
        excl_achiev_num: int = len(exclusive_achiev)

        if not exclusive_achiev:
            print(f"No exclusive Achievements for Player {i} :(\n")
        else:
            print(f"** {excl_achiev_num} Exclusive "
                  f"Achievements for Player {i}: {exclusive_achiev}\n")
        i += 1
    tot_achiev: set = set(achievements)
    i = 1
    for player in players:
        achiev_left: set = set.difference(tot_achiev, player)
        print(f"* Player {i} is missing: {achiev_left}\n")
        i += 1
