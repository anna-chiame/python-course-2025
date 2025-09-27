# Task 1
# Predefined variables
name = "Anna"
day = "Friday"
print(f"Good day {name}! {day} is a perfect day to learn some Python.") # using f/string
print("Good day {}! {} is a perfect day to learn some Python.".format(name, day)) # str.format()
print("Good day %s! %s is a perfect day to learn some Python." % (name, day), end="\n\n\n") # % format

#Task 2
first_name = "Anna"
last_name = "Chernets"
full_name = first_name + " " + last_name # concatenation with a space in between
print("Hello,", full_name + "!", end='\n\n\n') # Print a greeting

#Task 3
a = 100
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Division:", a / b)
print("Multiplication:", a * b)
print("Exponent (Power):", a ** b)
print("Modulus:", a % b)
print("Floor division:", a // b) 