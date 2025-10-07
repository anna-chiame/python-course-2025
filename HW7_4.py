# list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# dictionary -  number to day
num_to_day = {i+1: days[i] for i in range(len(days))}

# reverse dictionary - day to  number
day_to_num = {day: i+1 for i, day in enumerate(days)}

print(num_to_day)
print(day_to_num)