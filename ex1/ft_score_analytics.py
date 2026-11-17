import sys


def isInt(args: list) -> list:
    scores_list: list = []
    score: int
    for arg in args:
        try:
            score = int(arg)
            scores_list.append(score)
        except ValueError:
            print(f"Invalid input... Parameter {arg}"
                  " is not a number >n<")
    return scores_list


def ft_score_analytics(scores: list, players: int) -> None:
    score_list: list
    try:
        score_list = isInt(scores)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Number of players: {players}")
    print(f"Scores: {score_list}")
    print(f"Min score: {min(score_list)}")
    print(f"Max score: {max(score_list)}")
    print(f"Score Range: {max(score_list) - min(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / players}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    num_arg: int = len(sys.argv)
    args: list = sys.argv
    argsPrint: list = sys.argv[1:]
    if num_arg == 1:
        print("Not enough arguments provided :/")
    else:
        ft_score_analytics(argsPrint, (num_arg - 1))
