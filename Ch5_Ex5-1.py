# The 'time' module provides a function, also named 'time', that returns the current GMT in "the epoch", which is an
# arbitrary time used as a reference point. On UNIX systems, the epoch is January 1st, 1970.

import time
print(time.time())

# Write a script that reads the current time and converts it to a time of day in hours, minutes and seconds, plus the
# number of days since the epoch.

epoch = time.time()

# Variables used for more clarity in further calculations.
seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60
seconds_today = int(epoch % seconds_per_day)

# Calculating output variables.
hour = seconds_today // seconds_per_hour
minute = (seconds_today % seconds_per_hour) // seconds_per_minute
seconds = seconds_today - (hour * seconds_per_hour) - (minute * seconds_per_minute)
days_since_epoch = int(epoch // seconds_per_day)

print(f"It's {hour:02d}:{minute:02d}:{seconds:02d} on day {days_since_epoch} of the epoch.")
