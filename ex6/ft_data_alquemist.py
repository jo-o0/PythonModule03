import random


players: tuple = (
    "Paco",
    "Ernesto",
    "Josefina",
    "maritere",
    "Marga",
    "pepe sastre",
    "ur mom",
    "Juanita"
)


if __name__ == "__main__":
    print("=== GAME DATA ALCHEMIST ===")
    all_players: list = list(players)
    print(f"\n *** INITIAL LIST OF PLAYERS:\n {all_players}")
    cap: list = [name for name in players if name[0].isupper()]
    print(f"\n *** LIST WITH CAPITALIZED NAMES:\n {cap}")
    all_cap: list = [name.title() for name in players]
    print(f"\n *** LIST WITH ALL CAPITALIZED NAMES:\n {all_cap}")
    scores: dict[str, int] = {name: random.randint(0, 1000)
                              for name in all_cap}
    print(f"\n *** SCORE DICT: \n {scores}")
    i: int
    num_players: int = len(all_cap)
    media: float = round((sum(scores.values()) / num_players), 2)
    print(f"\n *** AVERAGE SCORE: {media}")
    high_scores: dict = {name: value for name,
                         value in scores.items() if value > media}
    print(f"\n *** PLAYERS WITH THE HIGHESTS SCORES:\n {high_scores}")
