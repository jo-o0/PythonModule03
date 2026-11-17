import typing
import random


players: tuple = (
    "Paco",
    "Ernesto",
    "Josefina",
    "Maritere",
    "Marga",
    "Pepe",
    "ur mom"
)

events: tuple = (
    "move",
    "steal",
    "arriquitraun",
    "shoot",
    "sleep",
    "run",
    "cook",
    "scape",
    "deathdrop"
)


def gen_events() -> typing.Iterator[tuple[str, str]]:
    while True:
        name: str = random.choice(players)
        action: str = random.choice(events)
        yield (name, action)


def consume_events(events) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index: int = random.randrange(len(events))
        yield (events.pop(index))


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("==== Generating 1000 random events ====")
    e: typing.Iterator[tuple[str, str]] = gen_events()
    player: str
    action: str
    player, action = next(e)
    i: int = 0
    while i < 1000:
        player, action = next(e)
        print(f"Event {i}: Player {player} did action {action}")
        i += 1
    i = 0
    event_list: list = []
    while i < 10:
        event_list.append(next(e))
        i += 1
    print("\n ==== CREATING A RANDOM EVENT LIST ====")
    print(f"\n *** RANDOMIZED LIST:\n {event_list}\n")
    for event in consume_events(event_list):
        player, action = event
        left: int = len(event_list)
        print(f"    * Player {player} did action {action}")
        print(f"      {left} events left\n")
        left -= 1
    print("=== End of Program ===")
