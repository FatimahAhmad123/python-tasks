#!/usr/bin/python3
import os

# Define the file path
file_path = "/home/nabeel/Desktop/python-tasks/task-5/my_dummy_file.txt" 

if not os.path.exists(file_path):
    try:
        with open(file_path, "w") as file: # "w" for writing to file
            file.write("New file created.")
        print(f"File created: {file_path}")
    except Exception as e:
        print(f"Error creating the file: {str(e)}")
        
# Add some text to the file
try:
    with open(file_path, "a") as file: # "a" for append mode
        file.write("\nNew line added.")
    print("New line added to the file.")
except Exception as e:
    print(f"Error adding text to the file: {str(e)}")

# Run the chmod command to change permissions
try:
    os.system(f"chmod a=- {file_path}")
    print("File permissions changed.")
except Exception as e:
    print(f"Error changing file permissions: {str(e)}")


# Open and read the file
try:
    with open(file_path, "r") as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"Error reading the file: {str(e)}")