#!/usr/bin/python3
import argparse
import math

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument for the coordinates
parser.add_argument(
    "--x1",
    type=float,
    help="Coordinates in the format 'x1,y1,x2,y2'",
)

parser.add_argument(
    "--y1",
    type=float,
    help="Coordinates in the format 'x1,y1,x2,y2'",
)

parser.add_argument(
    "--x2",
    type=float,
    help="Coordinates in the format 'x1,y1,x2,y2'",
)

parser.add_argument(
    "--y2",
    type=float,
    help="Coordinates in the format 'x1,y1,x2,y2'",
)

# Parse the command-line arguments
args = parser.parse_args()

# Extract the coordinates as a string
x1 = args.x1
x2 = args.x2
y1 = args.y1
y2 = args.y2

# Split the string into individual values
# x1, y1, x2, y2 = map(float, coordinates_str.split(","))

# Calculate the distance
distance = math.dist([x1, y1], [x2, y2])

# Print the result
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.3f} units.")
