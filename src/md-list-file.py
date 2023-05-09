import os

directory = input("Enter Path:" +" ")

output_file = os.path.join(directory, "checklist.md")

print(f"Creating output file: {output_file}")

with open(output_file, "w") as f:
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_basename, file_extension = os.path.splitext(filename)
            f.write(f"- [ ] {os.path.basename(file_basename)}\n")
                                    
print("Done.")
