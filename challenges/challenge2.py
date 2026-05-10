# challenge2.py — Two-Column Report
# Read favorites.csv, find the most common problem per language, print a table.

import csv

# Your code here
import csv
from pathlib import Path
counts = {}
with open(csv_path, "r", newline="") as file:
reader = csv.DictReader(file)
for row in reader:
language = row["language"]
problem = row["problem"]
if language not in counts:
counts[language] = {}
counts[language][problem] = counts[language].get(problem, 0) + 1
print("Language | Most Common Problem")
print("-----------+--------------------")
for language in sorted(counts):
most_common = max(counts[language], key=counts[language].get)
print(f"{language:<10} | {most_common}")
