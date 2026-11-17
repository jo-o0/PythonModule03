import math


def ft_input() -> tuple:
    coordinates: list = []
    while True:
        try:
            coordinates.append(float(input("Introduce X: ")))
            break
        except ValueError:
            print("Invalid 'X' value, please enter a numerical value")
    while True:
        try:
            coordinates.append(float(input("Introduce Y: ")))
            break
        except ValueError:
            print("Invalid 'Y' value, please enter a numerical value")
    while True:
        try:
            coordinates.append(float(input("Introduce Z: ")))
            break
        except ValueError:
            print("Invalid 'Z' value, please enter a numerical value")
    return tuple(coordinates)


def get_player_pos() -> None:
    coord_list: tuple[float, float, float] = ft_input()
    pos: list = ["X", "Y", "Z"]
    i: int = 0
    print("Got a point with the next coordinates:")
    for coord in coord_list:
        print(f"Position {pos[i]}: {coord}")
        i += 1
    print("Let´s calculate the distance from the center...")
    dist_center: float
    dist_center = math.sqrt((coord_list[0] - 0)**2 +
                            (coord_list[1] - 0)**2 +
                            (coord_list[2] - 0)**2)
    print(f"The distance from the center is: {dist_center}")
    print("Enter another set of coordinates")
    new_coord: tuple[float, float, float] = ft_input()
    print("Got a new point with the next coordinates:")
    i = 0
    for coordnts in new_coord:
        print(f"Position {pos[i]}: {coordnts}")
        i += 1
    new_dist: float
    new_dist = math.sqrt((new_coord[0] - coord_list[0])**2 +
                         (new_coord[1] - coord_list[1])**2 +
                         (new_coord[2] - coord_list[2])**2)
    print(f"Distance between the two given points is: {new_dist}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()
    print("=== End of the program ===")
