import os

labels_path = "dataset/labels/2010.txt"  # Update with a real filename

with open(labels_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Print first 10 lines to check the format
for line in lines[:10]:
    print(line.strip())  # Remove extra spaces or new lines
