# starter.py — Language Poll Analyser
# Project 1 | Easy | 20–25 minutes
#
# Run from this folder:
#   python starter.py
#
# The CSV file is at: ../../week1/favorites.csv

import csv

# ── Step 1: Read the CSV and count languages ──────────────────────────────────
counts = {}

with open("../../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # TODO: Get the language from the row
        language = ???

        # TODO: Update counts — increment if exists, create if new
        ???

# ── Step 2: Sort by popularity (most popular first) ───────────────────────────
# Hint: sorted(counts, key=counts.get, reverse=True)
sorted_languages = ???

# ── Step 3: Print the report ──────────────────────────────────────────────────
print("=== Language Popularity Report ===")

# TODO: Loop over sorted_languages with enumerate() to get rank numbers (start=1)
# Format each line like: "1. Python  : 196 students"
for rank, language in ???:
    ???

# TODO: Print the total number of responses
# Hint: sum(counts.values())
print(f"\nTotal responses: ???")
import csv
from pathlib import Path
counts = {}
with open(csv_path, "r", newline="") as file:
reader = csv.DictReader(file)
for row in reader:
language = row["language"]
counts[language] = counts.get(language, 0) + 1
sorted_languages = sorted(counts, key=counts.get, reverse=True)
print("=== Language Popularity Report ===")
for rank, language in enumerate(sorted_languages, start=1):
print(f"{rank}. {language:<8}: {counts[language]} students")
print(f"Total responses: {sum(counts.values())}")

