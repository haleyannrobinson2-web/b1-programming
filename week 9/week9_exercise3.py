# file manager with os module

import os

# 1. Display current working directory
print("Current Working Directory:")
print(os.getcwd())


# 2. Create a new folder called "lab_files"
folder_name = "lab_files"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'Folder "{folder_name}" created successfully.')
else:
    print(f'Folder "{folder_name}" already exists.')


# 3. Create three empty text files inside that folder
file_names = ["file1.txt", "file2.txt", "file3.txt"]

for file in file_names:
    file_path = os.path.join(folder_name, file)
    with open(file_path, "w") as f:
        pass   # creates empty file
    print(f'File "{file}" created.')


# 4. List all files in the folder
print("\nFiles inside the folder:")
files = os.listdir(folder_name)
for file in files:
    print(file)


# 5. Rename one of the files
old_name = os.path.join(folder_name, "file1.txt")
new_name = os.path.join(folder_name, "renamed_file.txt")

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print('\nFile "file1.txt" renamed to "renamed_file.txt".')
else:
    print("File to rename not found.")


# Show updated file list
print("\nUpdated file list:")
files = os.listdir(folder_name)
for file in files:
    print(file)


# 6. Clean up (remove files and folder)
print("\nCleaning up...")

for file in os.listdir(folder_name):
    file_path = os.path.join(folder_name, file)
    os.remove(file_path)
    print(f'File "{file}" deleted.')

os.rmdir(folder_name)
print(f'Folder "{folder_name}" deleted successfully.')