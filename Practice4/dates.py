# dates.py

from datetime import datetime

now = datetime.now()

print("Current Date and Time:")
print(now)

print("\nFormatted Date:")
print(now.strftime("%d/%m/%Y"))


date1 = datetime(2026, 2, 1)
date2 = datetime(2026, 2, 14)

difference = date2 - date1

print("\nDifference in Days:")
print(difference.days)
