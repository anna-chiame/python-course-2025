numbers_1 = []
i = 1
while i <= 100:
   numbers_1.append(i)
   i += 1

numbers_2 = []
# iterate through all_numbers using a while loop
i = 0
while i < len(numbers_1):
    num = numbers_1[i]
    if num % 7 == 0 and num % 5 != 0:  # divisible by 7 but not by 5
       numbers_2.append(num)
    i += 1
print("Our Extractes numbers are:\n", numbers_2)
