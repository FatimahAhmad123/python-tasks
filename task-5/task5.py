#!/usr/bin/python3
import os

# Define the file path
file_path = "/home/nabeel/Desktop/python-tasks/task-5/my_dummy_file.txt" 

#Check if exixts otherwise create file
if not os.path.exists(file_path):
    with open(file_path, "w") as file: # "w" for writing to file
        file.write("New file created.")
    print(f"File created: {file_path}")

        
# Add some text to the file
with open(file_path, "a") as file: # "a" for append mode
    file.write("\nNew line added.")
print("New line added to the file.")

# Run the chmod command to change permissions
os.system(f"chmod a=- {file_path}")
print("File permissions changed.")


# Open and read the file
try:
    with open(file_path, "r") as file:
        content = file.read()
    print("File content:")
    print(content)
except Exception as e:
    print(f"Error reading the file: {str(e)}")