# Practice using the Python interpreter as a calculator.


# 1. The volume of a sphere with radius r is '(4 ⁄ 3) π r**3'. What is the volume of a sphere with radius 5.
import math

r = 5
v = (4 / 3) * math.pi * r**3
print(v)

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping cost $3 for the first copy
# and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

price = 24.95
discounted_price = price * 0.6
shipping_cost_1 = 3
shipping_cost_2 = 0.75
n_copies = 60

cost = discounted_price * n_copies + shipping_cost_1 + (n_copies-1)*shipping_cost_2
print(cost)
print(f"{cost:.2f}")  # Output formatted to two decimal places.

# 3. If I leave my house at 6:52am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
# and 1 mile at an easy pace again, what time do I get home for breakfast?

departure_hour = 6
departure_minute = 52

easy_pace_minutes = 8
easy_pace_seconds = 15
tempo_pace_minutes = 7
tempo_pace_seconds = 12

distance_easy_pace = 2
distance_tempo_pace = 3

final_time_minutes = (easy_pace_minutes * distance_easy_pace) + (tempo_pace_minutes * distance_tempo_pace)
final_time_seconds = (easy_pace_seconds * distance_easy_pace) + (tempo_pace_seconds * distance_tempo_pace)

if final_time_seconds >= 60:
    final_time_seconds -= 60
    final_time_minutes += 1

print(f"The run lasted {final_time_minutes}:{final_time_seconds:02d} minutes.")

arrival_hour = 0
arrival_minute = departure_minute + final_time_minutes

if arrival_minute >= 60:
    arrival_hour += 1
    arrival_minute -= 60

arrival_hour += departure_hour

print(f"You arrive at home at {arrival_hour}:{arrival_minute:02d} for breakfast.")
