# Convert Hours to Seconds
"""
60 seconds = 1 min
60 minutes = 1 hr
120 minutes = 2hrs
"""
hours = 2
one_minutes_to_seconds = 60 # Seconds
one_hour_to_minutes = 60 # minutes

# one hour to seconds

hour_to_seconds = one_minutes_to_seconds * one_hour_to_minutes

#final conversion of 2 hours to seconds
seconds = hours * hour_to_seconds

print("2 hour(s) is", seconds, "seconds")
