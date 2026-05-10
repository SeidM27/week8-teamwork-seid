# challenge3.py — CSV Writer
# Read favorites.csv, count votes per language, write results to language_summary.csv.

import csv

# Your code here
import csv
from pathlib import Path
counts = {}
total = 0
with open(csv_path, "r", newline="") as file:
reader = csv.DictReader(file)
for row in reader:
language = row["language"]
counts[language] = counts.get(language, 0) + 1
total += 1
with open(output_path, "w", newline="") as file:
writer = csv.DictWriter(file, fieldnames=["language", "votes", "percentage"])
writer.writeheader()
for language in sorted(counts, key=counts.get, reverse=True):
percentage = (counts[language] / total) * 100
writer.writerow({
