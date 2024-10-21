
#Program allowing a user to specify a time of the day and add the number
#of hour later they would like and alarm to go off.

current_time = int(input("What is the current time (in hours 1-24)? "))
hours_to_wait = int(input("How many hours do you want to wait? "))

future_time = (current_time + hours_to_wait) % 24

print("The alarm will go off at", future_time)
