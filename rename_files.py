import os
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Get the current directory
current_directory = os.getcwd()

# Get a list of all the files in the current directory
files = os.listdir(current_directory)

# Iterate over all the files
for file in files:
    if file == "rename_files.py":
        continue
    # Get the file's creation time
    creation_time = os.path.getctime(file)

    # Create a new file name based on the creation time
    new_file_name = datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d-%H:%M:%S") + "-" + file

    # Rename the file
    os.rename(file, new_file_name)

print("All files have been renamed.")
