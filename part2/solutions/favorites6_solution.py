# favorites6_solution.py
import csv

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        try:
            counts[favorite] += 1
        except KeyError:
            counts[favorite] = 1

for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
import csv
from pathlib import Path
counts = {}
with open(csv_path, "r", newline="") as file:
reader = csv.DictReader(file)
for row in reader:
favorite = row["language"]
try:
counts[favorite] += 1
except KeyError:
counts[favorite] = 1
for favorite in counts:
print(f"{favorite}: {counts[favorite]}")
