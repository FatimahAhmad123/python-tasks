#!/usr/bin/python3
import argparse
import math


def main():
    parser = argparse.ArgumentParser(
        description="Calculate the distance between two coordinates."
    )
    parser.add_argument(
        "coordinates", nargs=4, help="Coordinates in the format 'x1,y1 x2,y2'"
    )

    args = parser.parse_args()

    coordinates = args.coordinates
    x1, y1, x2, y2 = map(float, [coord.replace(",", " ") for coord in coordinates])

    p = [x1, y1]
    q = [x2, y2]

    distance = math.dist(p, q)
    print(
        f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f} units."
    )


if __name__ == "__main__":
    main()
