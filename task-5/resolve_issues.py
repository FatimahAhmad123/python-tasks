#!/usr/bin/python3
import os

# Define the file path
file_path = "/home/nabeel/Desktop/python-tasks/task-5/my_dummy_file.txt" 

# Modify the file permissions to allow reading

os.system(f"chmod +r {file_path}")
print("File permissions modified to allow reading.")

# Attempt to read the file
try:
    with open(file_path, "r") as file:
        content = file.read()
    print("File content:")
    print(content)
except Exception as e:
    print(f"Error reading the file: {str(e)}")
