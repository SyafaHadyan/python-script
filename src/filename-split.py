import os

input_directory = input("Folder path:")

for filename in os.listdir(input_directory):
    if '_' in filename:
        split_filename = filename.split('_')
        try:
            int(split_filename[1])
            new_filename = ' '.join(split_filename[0:1])
            os.rename(os.path.join(input_directory, filename), os.path.join(input_directory, new_filename))
        except ValueError:
            continue
