# challenge1.py — Frequency Filter
# Read favorites.csv, ask for a minimum vote count, print filtered results.
# No starter hints — build this from scratch using what you learned in week1 and week2.

import csv

# Your code here
import csv
from pathlib import Path
minimum = int(input("Minimum votes to display: "))
counts = {}
with open(csv_path, "r", newline="") as file:
reader = csv.DictReader(file)
for row in reader:
language = row["language"]
counts[language] = counts.get(language, 0) + 1
for language in sorted(counts, key=counts.get, reverse=True):
if counts[language] >= minimum:
print(f"{language}: {counts[language]}")
