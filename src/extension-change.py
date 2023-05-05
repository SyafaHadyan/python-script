import os

input_directory = input("Folder path:")
directory = input_directory

input_old = input("Extension to convert:")
old_extension = "." + input_old

input_new = input("New extension:")
new_extension = "." + input_new

for filename in os.listdir(directory):
    if filename.endswith(old_extension):
        new_filename = os.path.splitext(filename)[0] + new_extension
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
