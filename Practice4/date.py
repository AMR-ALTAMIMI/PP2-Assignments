Task 1: Subtract Five Days from Current Date
from datetime import datetime, timedelta

# Get the current date and time
current_date = datetime.now()

# Subtract 5 days
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date 5 Days Ago:", new_date)



Task 2: Print Yesterday, Today, and Tomorrow
from datetime import datetime, timedelta

# Get today's date
today = datetime.now()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())



Task 3: Drop Microseconds from Datetime
from datetime import datetime

# Get current date and time
current_time = datetime.now()

# Remove microseconds
new_time = current_time.replace(microsecond=0)

print("Original Datetime:", current_time)
print("Without Microseconds:", new_time)



Task 4: Calculate Difference Between Two Dates in Seconds
from datetime import datetime

# Define two dates
date1 = datetime(2026, 6, 20, 10, 30, 0)
date2 = datetime(2026, 6, 27, 12, 45, 30)

# Calculate the difference
difference = date2 - date1

# Convert difference to seconds
seconds = difference.total_seconds()

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in Seconds:", seconds)
