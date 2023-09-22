#!/usr/bin/python3
import os

# Define the file path
file_path = "/home/user/Desktop/my_dummy_file.txt"

# Step 1: Ensure the file has appropriate permissions (e.g., read and write for the user)
try:
    os.system(f"chmod u+rw {file_path}")
    print("File permissions updated successfully.")
except Exception as e:
    print(f"Error: {str(e)}")

# Step 2: Attempt to read and write to the file again
try:
    with open(file_path, "r") as file:
        content = file.read()
    with open(file_path, "a") as file:
        file.write("\nMore text added.")
    print("File read and write successful after resolving permissions.")
except Exception as e:
    print(f"Error: {str(e)}")
