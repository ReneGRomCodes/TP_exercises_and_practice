# Start the Python interpreter and use it as a calculator.


# 1. How many seconds are there in 42 minutes, 42 seconds?

minutes = 42
seconds = 42
answer = minutes * 60 + seconds
print(answer)

# Alternative solution including user input:
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
answer = minutes * 60 + seconds
print(answer)

# Another alternative using different input format:
t = input("Enter time in mm:ss format: ")
minutes_seconds = t.split(":")
answer = int(minutes_seconds[0]) * 60 + int(minutes_seconds[1])
print(answer)


# 2. How many miles are there in 10 kilometers?

kilometers = 10
answer = kilometers / 1.6
print(answer)


# 3. If you run a 10-kilometer race in 42 minutes, 42 seconds, what is your average pace (time per mile in minutes and
# seconds)? What is your average speed in miles per hour?

distance_km = 10
t_minutes = 42
t_seconds = 42
distance_miles = distance_km / 1.6
minutes_to_seconds = t_minutes * 60

# Calculating pace.
pace_minutes = int((minutes_to_seconds) / distance_miles // 60)
pace_seconds = int((minutes_to_seconds) / distance_miles % 60)
print(f"Pace (time per mile) is {pace_minutes}:{pace_seconds}.")

# Calculating average speed.
seconds_per_hour = 3600
time_for_distance_seconds = minutes_to_seconds + t_seconds
average_speed = round(distance_miles / time_for_distance_seconds * seconds_per_hour, 2)
print(f"Average speed is {average_speed} miles per hour.")
