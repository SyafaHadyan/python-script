import os

directory = input("Enter Path:" + " ")

output_file = os.path.join(directory, "checklist.md")

with open("checklist.md", "w") as f:
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_basename, file_extension = os.path.splitext(filename)
            f.write(f"- [ ] {file_basename}\n")
