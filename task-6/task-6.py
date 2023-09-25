#!/usr/bin/python3
import matplotlib.pyplot as plt
from calculations import calculate_square, calculate_cube

# Read data from the file and convert to a list
with open("dummy_file.txt", "r") as file:
    data = [int(x) for x in file.readline().strip().split(",")]

# Calculate square and cube
square_data = calculate_square(data)
cube_data = calculate_cube(data)

# Plot the graph
plt.plot(data, square_data, label="Square")
plt.plot(data, cube_data, label="Cube")

# Add labels and legend
plt.xlabel("Data")
plt.ylabel("Value")
plt.legend()

# Display the plot
plt.show()
