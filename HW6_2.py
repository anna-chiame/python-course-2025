import random

numbers_1 = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    numbers_1.append(num)
    i += 1
print("Our random numbers in the 1st list:\n", numbers_1)

numbers_2 = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    numbers_2.append(num)
    i += 1
print("Our random numbers in the 2nd list:\n", numbers_2)

#create a list for common numbers without duplicates
common_numbers = []
i = 0
while i < len(numbers_1):
# add only if number is in both lists and not already added
    if numbers_1[i] in numbers_2 and numbers_1[i] not in common_numbers:
        common_numbers.append(numbers_1[i])
    i += 1
print("List of common numbers without duplicates:", common_numbers)


