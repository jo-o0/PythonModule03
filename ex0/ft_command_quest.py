import sys


def ft_command_quest(arg: str, index: int):
    print(f"Argument {index}: {arg}")


if __name__ == "__main__":
    num_arg: int = len(sys.argv)
    print("=== Commad Quest ===")
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments provided: {num_arg - 1}")
    if num_arg == 1:
        print("No arguments provided!")
    else:
        index: int = 1
        for arugment in sys.argv[1:]:
            ft_command_quest(arugment, index)
            index += 1
    print(f"Total arguments: {num_arg}")
