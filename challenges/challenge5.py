# challenge5.py — Data Cleaner
# Read a messy CSV, detect problems, write a cleaned version, print a report.
# Create your own messy_data.csv with intentional errors to test against.

import csv

# Your code here
import csv
from pathlib import Path
allowed_languages = {"Python", "C", "Scratch"}
seen_ids = set()
cleaned_rows = []
blank_rows = 0
duplicate_ids = 0
bad_scores = 0
unknown_languages = 0
with open(input_file, "r", newline="") as file:
reader = csv.DictReader(file)
for row in reader:
if not any(value.strip() for value in row.values()):
blank_rows += 1
continue
student_id = row["student_id"].strip()
language = row["language"].strip().title()
if student_id in seen_ids:
duplicate_ids += 1
