# challenge4.py — SQL Explorer
# Present an interactive menu that runs different SQL queries on favorites.db.
# Requires favorites.db — see week2/README.md for setup instructions.

import sqlite3

# Your code here
import sqlite3
from pathlib import Path
connection.row_factory = sqlite3.Row
while True:
print("\n=== SQL Explorer ===")
print("1. Count by language")
print("2. Count by problem")
print("3. Search by problem name")
print("4. Top 5 problems overall")
print("5. Quit")
choice = input("Choice: ")
if choice == "1":
rows = cursor.execute(
"SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC"
).fetchall()
for row in rows:
print(f"{row['language']}: {row['n']}")
elif choice == "2":
rows = cursor.execute(
"SELECT problem, COUNT(*) AS n FROM favorites GROUP BY problem ORDER BY n DESC"
).fetchall()
for row in rows:
print(f"{row['problem']}: {row['n']}")
elif choice == "3":
problem = input("Problem name: ")
rows = cursor.execute(
"SELECT language, COUNT(*) AS n FROM favorites WHERE problem = ? GROUP BY language ORDER BY n DESC",
(problem,)
).fetchall()
for row in rows:
print(f"{row['language']}: {row['n']}")
elif choice == "4":
rows = cursor.execute(
"SELECT problem, COUNT(*) AS n FROM favorites GROUP BY problem ORDER BY n DESC LIMIT 5"
).fetchall()
for row in rows:
print(f"{row['problem']}: {row['n']}")
elif choice == "5":
break
else:
print("Invalid choice.")

